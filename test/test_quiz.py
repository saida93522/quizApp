from unittest import TestCase
from unittest.mock import patch
from db_script import Quize_Table, QuizError
import os
import csv
import sqlite3
test_file = 'test.csv'
rows = [['questions'], ['correct'], ['wrong1'], ['wrong2'], ['wrong3'],
        ['category'], ['difficulty'], ['possible_points']]


class TestQuiz(TestCase):

    def setUp(self):  # Arrange
        "set up temporary database and populate it with some data"
        test_quiz = os.path.join('database', 'test_quiz_records.db')
        self.quiz = Quize_Table()
        Quize_Table.instance = None

    def test_available_category_is_empty(self):
        list_topic = []
        self.assertIsNotNone(list_topic, self.quiz.display_category())

    def test_display_category(self):
        list_topic = ['art', 'space', 'sport']
        self.assertListEqual(list_topic, self.quiz.display_category())

    def test_get_questions_art(self):
        topic = 'art'
        qs_attempt = 2
        list_questions = ['Who painted the Mona Lisa?',
                          "What precious stone is used to make the artist's pigment ultramarine?"]
        self.assertEqual(
            list_questions, self.quiz.get_questions(topic, qs_attempt))

    def test_get_questions_space(self):
        topic = 'space'
        qs_attempt = 3
        list_questions = ['Which planet has the fastest rotation?',
                          'Which planet is closest to the sun?', 'Which planet spins in the opposite direction to all the others in the solar system?']
        self.assertEqual(
            list_questions, self.quiz.get_questions(topic, qs_attempt))

    def test_get_questions_sport(self):
        topic = 'sport'
        qs_attempt = 5
        list_questions = ["Which gymnast is the 'triple-twisting double-tucked salto backwards skill named after'?",
                          'The Olympics are held every how many years?', 'How many players are on a baseball team?', 'What color are the goalposts in football?', 'What’s the national sport of Canada?']
        self.assertEqual(
            list_questions, self.quiz.get_questions(topic, qs_attempt))

    def test_available_questions_empty(self):
        topic = 'space'
        qs_attempt = 0
        list_questions = []
        self.assertEqual(
            list_questions, self.quiz.get_questions(topic, qs_attempt))

    def test_question_count(self):
        topic = 'art'
        self.assertEqual(5, self.quiz.get_question_count(topic))

    def test_question_count_is_not_zero(self):
        topic = 'space'
        self.assertNotEqual(0, self.quiz.get_question_count(topic))

    def test_possible_answers(self):
        question = 'Which planet has the fastest rotation?'
        choices = ['Jupiter', 'Neptune', 'Venus', 'Mars']
        self.assertCountEqual(
            choices, self.quiz.get_possible_answers(question))

    def test_multiple_answers_is_not_less(self):
        question = 'What’s the national sport of Canada?'
        choices = ['Hockey', 'Soccer', 'Baseball']
        self.assertNotEqual(choices, self.quiz.get_possible_answers(question))

    def test_get_answer_correct(self):
        question = "Which gymnast is the 'triple-twisting double-tucked salto backwards skill named after'?"
        answer = 'Simone Biles'
        self.assertTrue(answer, self.quiz.get_answer(question))

    def test_get_answer_wrong(self):
        question = "Which gymnast is the 'triple-twisting double-tucked salto backwards skill named after'?"
        answer = 'Jupiter'
        self.assertNotEqual(answer, self.quiz.get_answer(question))

    def test_points(self):
        question = 'Which country is The Louvre art museum located?'
        point = 2
        points = 0
        self.assertEqual(point, self.quiz.get_possible_points(question))
        self.assertNotEqual(points, self.quiz.get_possible_points(question))

    def test_difficulty(self):
        question = 'Who painted the Mona Lisa?'
        difficulty = 2
        self.assertTrue(difficulty, self.quiz.get_range(question))
        self.assertNotEqual(1, self.quiz.get_range(question))

    def test_get_answer_by_id(self):
        question = 'Which planet spins in the opposite direction to all the others in the solar system?'
        question_id = 8
        self.assertTrue(question_id, self.quiz.get_question_by_id(question))
        self.assertNotEqual(2, self.quiz.get_question_by_id(question))
        self.assertTrue(-1, self.quiz.get_question_by_id(question))

    def test_get_answer_by_id_question_not_found(self):
        question = 'Which planet spins in the opposite direction to all the others in the solar system?'
        question_id = 2
        with self.assertRaises(QuizError):
            if question_id == None:
                self.quiz.get_question_by_id(question)
