""" Program displays the available topics from the database as well as the number of questions for that topic. """
# use class variable for storing sessions
from db_script import Quize_Table
import ui
import valid as valid
import random
import sys
quiz = Quize_Table()


def main():
    ui.welcome_banner()
    while True:
        topic = valid.check_topic_input()
        display_questions(topic)


def display_questions(topic):
    topic, num_questions = topic
    questions = quiz.get_questions(topic, num_questions)
    total_incorrect = []
    total_score = []

    for question in questions:
        print(question, display_range(question),
              display_points_available(question))
        display_choices(question)

        user_answer = input('Enter your answer here: ')
        correct_answer = display_answer(question)
        check = valid.check_user_answer(user_answer, correct_answer)
        score = get_Score(question)
        if check:
            total_score.append(score)
        else:
            total_incorrect.append('incorrect')

    print(sum(total_score), total_incorrect, user_answer)
    return quiz.add_entry(topic[0], user_answer, score, total_incorrect)


def display_choices(question):
    answers = quiz.get_possible_answers(question)
    return ui.show_choice(answers)


def display_points_available(question):
    points = quiz.get_possible_points(question)
    return ui.show_possible_points(points)


def display_range(question):
    difficulty_range = quiz.get_range(question)
    return ui.get_range(difficulty_range)


def display_answer(question):
    correct = quiz.get_answer(question)
    return correct


def get_Score(question):
    score = quiz.get_score(question)
    return score


main()
