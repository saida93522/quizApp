import sys
"Verifies that the user entered the correct input"
from db_script import Quize_Table
quiz = Quize_Table()


def check_topic_input():
    while True:
        topic = input('Enter a topic(art,space,sport): ').lower()
        if topic == 'quit':
            sys.exit()
        user = quiz.display_category()
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
            user = quiz.get_question_count(topic)
            if num_question > user or num_question <= 0:
                print(
                    f'sorry there is a maximum of {user} question available. Try again')
            else:
                return num_question
        except ValueError:
            print('Enter number only')


def check_user_answer(user_answer, correct_answer):
    if user_answer == correct_answer.lower():
        print('corret')
        return True
    else:
        print(
            f'sorry that was incorrect, the corect answer is {correct_answer}\n')
        return False
