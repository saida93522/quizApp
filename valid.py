import sys
import ui
from db_script import Quize_Table
quiz = Quize_Table()


def check_topic_input():  
    """ verifies that the user entered the correct input """

    while True:
        topic = ui.ask_question('Enter a topic(art,space,sport): ').lower()
        if topic == 'quit':
            return topic
        user = quiz.display_category()  # is user the best variable name? 
        if topic in user:
            num_questions = check_num_input(topic)
            print(
                f'You chose to answer {num_questions} from the {topic} category')
            return topic, num_questions
        else:
            print('Not a valid topic try again.')


def check_num_input(topic):
    while True:
        try:
            num_question = int(
                input('Enter the number of questions you would like to attempt: '))
            user = quiz.get_question_count(topic) # is user the best variable name? 
            if num_question > user or num_question <= 0:
                print(
                    f'sorry there is a maximum of {user} question available. Try again')
            else:
                return num_question
        except ValueError:
            print('Enter number only')
