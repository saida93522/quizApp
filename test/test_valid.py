from unittest import TestCase
# from unittest.mock import patch
import os
import db_script
from db_script import Quize_Table


class TestValid(TestCase):

    def setUp(self):
        quiz_path = os.path.join('database', 'test_quiz_records.db')
        self.quiz = Quize_Table()
        Quize_Table.instance = None

    def test_check_user_input(self):
        self.assertIn('art', self.quiz.display_category())
        self.assertIn('space', self.quiz.display_category())
        self.assertNotIn('aliens', self.quiz.display_category())

    def test_check_num_input(self):
        self.assertTrue(5, self.quiz.get_question_count('art'))
        self.assertTrue(1, self.quiz.get_question_count('art'))
        self.assertFalse(0, self.quiz.get_question_count('art'))
        self.assertFalse(0, self.quiz.get_question_count('space'))
