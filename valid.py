"Verifies that the user entered the correct input"
from db_script import Quize_Table
quiz = Quize_Table()


def check_topic_input():
    while True:
        topic = input('Enter a topic(art,space,sport): ').lower()
        user = quiz.display_category()
        if topic in user:
            return topic
        else:
            print('Not a valid topic try again.')


def check_num_input(topic):
    while True:
        num_question = int(
            input('Enter the number of questions you would like to attempt: '))
        user = quiz.get_question_count(topic)
        if num_question > user or num_question <= 0:
            print(
                f'sorry there is a maximum of {user} question available. Try again')
        else:
            return num_question
