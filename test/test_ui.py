from unittest import TestCase
from unittest.mock import patch
from db_script import Quize_Table
import ui


class TestUI(TestCase):

    def setUp(self):
        self.quiz = Quize_Table()
        Quize_Table.instance = None

    # decorator that handles patching builtin module within the scope test
    @patch('builtins.print')
    def test_welcome_banner(self, mock_print):
        """ensuring expected output got printed to the terminal """
        ui.welcome_banner()  # action
        mock_print.assert_called()  # assert

    @patch('builtins.print')
    def test_show_question(self, mock_print):
        self.assertTrue(ui.show_question('is python a snake?', 2, 4))
        mock_print.assert_called()

    def test_show_question_wrong_data_type(self):
        self.assertFalse(ui.show_question(2, 4, 5))
        self.assertFalse(ui.show_question('is mango orange?', '4', 5))
        self.assertFalse(ui.show_question(
            ['one question', 'two question'], 4, '5'))

    def test_show_choices(self):
        answers = ['yes', 'no', 'maybe', 'idk']
        self.assertTrue(['no', 'yes', 'idk', 'maybe'],
                        ui.show_choice(answers))
        self.assertTrue(['idk', 'maybe', 'no', 'yes'],
                        ui.show_choice(answers))
        self.assertTrue(['yes', 'no', 'maybe', 'idk'],
                        ui.show_choice(answers))

    def test_check_user_answer(self):
        user = 'jupiter'
        correct = 'jupiter'
        self.assertTrue(ui.check_user_answer(user, correct))
        self.assertFalse(ui.check_user_answer('mars', correct))
