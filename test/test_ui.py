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
        # this checks if print was called at all. To be more specific,
        mock_print.assert_called()  # check that the print statement is called with the 'is python a snake' string 


    def test_show_question_wrong_data_type(self):
        self.assertFalse(ui.show_question(2, 4, 5))
        self.assertFalse(ui.show_question('is mango orange?', '4', 5))
        self.assertFalse(ui.show_question(
            ['one question', 'two question'], 4, '5'))

    def test_show_choices(self):
        answers = ['yes', 'no', 'maybe', 'idk']
        # show_choice doesn't return anything.  See notes on assertTrue in test_quiz.
        # the second argument is a message to print when the test fails.
        # but what these are checking is, the first argument, the list, is that True?
        # and lists with at least one element are Truthy, 
        # so ['no', 'yes', 'idk', 'maybe'] is truthy and the assert statement is happy
        # but these checks are not checking anything about your code.
        # Here you may want to mock print and verify it prints each answer one time. 
        self.assertTrue(['no', 'yes', 'idk', 'maybe'],
                        ui.show_choice(answers))
        self.assertTrue(['idk', 'maybe', 'no', 'yes'],
                        ui.show_choice(answers))
        self.assertTrue(['yes', 'no', 'maybe', 'idk'],
                        ui.show_choice(answers))

    def test_check_user_answer(self):
        # check correct answer is identified
        user = 'jupiter'
        correct = 'jupiter'
        self.assertTrue(ui.check_user_answer(user, correct))
    

    def test_check_user_answer_different_case(self):
        # check correct answer is identified, even with different case.  
        # You could add some more different combinations of upper and lowercase here too
        user = 'JuPitEr'
        correct = 'jupiter'
        self.assertTrue(ui.check_user_answer(user, correct))


    def test_check_user_answer_incorrect(self):
        # check wrong answer is identified 
        user = 'mars'
        correct = 'jupiter'
        self.assertTrue(ui.check_user_answer(user, correct))



