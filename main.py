""" Program displays the available topics from the database as well as the number of questions for that topic. """
# use class variable for storing sessions
from db_script import Quize_Table
import ui
import valid as valid
import random
quiz = Quize_Table()


def main():
    ui.welcome_banner()
    topic = valid.check_topic_input()
    print(topic)
    # if (acct == 'quit'): break
    num_questions = valid.check_num_input(topic)
    print(num_questions)
    display_questions(topic, num_questions)


def display_questions(topic, num_questions):
    questions = quiz.get_questions(topic, num_questions)

    for question in questions:
        points_avbl = display_points_available(question)
        diff_range = display_range(question)
        print(question, points_avbl, diff_range)

        display_choices(question)
        user_answer = ui.get_answer('Enter answer here: ').lower()
        correct = display_answer(question)
        if user_answer in correct.lower():
            print('Corret\n')

        else:
            print(
                f'sorry that was incorrect, the corect answer is {correct}\n')


def display_choices(question):
    answers = quiz.get_possible_answers(question)
    random.shuffle(answers)
    for answer in answers:
        print(f'\t* {answer}')


def display_points_available(question):
    points = quiz.get_possible_points(question)
    return f'worth ({points}) points - '


def display_range(question):
    difficulty_range = quiz.get_range(question)
    return f'difficulty({difficulty_range})'


def display_answer(question):
    correct = quiz.get_answer(question)

    return correct


main()
