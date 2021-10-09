from unittest import TestCase
import db_script as quiz_questions
from db_script import Quize_Table
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

    def test_available_category_is_displayed(self):
        list_topic = ['art', 'space', 'sport']
        self.assertEqual(list_topic,
                         self.quiz.display_category())

    def test_available_category_is_empty(self):
        list_topic = []
        self.assertIsNotNone(list_topic, self.quiz.display_category())

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
