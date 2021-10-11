""" Program displays the available topics from the database as well as the number of questions for that topic. """
# use class variable for storing sessions
from db_script import Quize_Table
import ui
import valid as valid
import random
import sys
import time
quiz = Quize_Table()

#!/usr/bin/env python


def main():
    ui.welcome_banner()
    while True:
        topic = valid.check_topic_input()
        display_questions(topic)


def display_questions(topic):
    """ displays list of questions 
    :param a tuple containing chosen topic and number of questions user wants to answer"""
    topic, num_questions = topic
    questions = quiz.get_questions(topic, num_questions)
    total_point_avbl = []
    total_score = []
    correct = []
    for question in questions:
        start_time = time.time()
        q_range = display_range(question)
        avble_points = display_points_available(question)
        total_point_avbl.append(avble_points)

        # print question
        ui.show_question(question, q_range, avble_points)
        display_choices(question)

        # get result
        score, counter_correct = get_response(question)
        total_score.append(score)
        correct.append(counter_correct)

    ui.show_result(start_time, num_questions, sum(correct),
                   sum(total_point_avbl), sum(total_score))


def get_response(question):
    """ get the user response and add data in quiz_result table  """
    user_answer = ui.ask_question('Enter your answer here: ')
    correct_answer = display_answer(question)
    # validate user entered correct answer
    check = ui.check_user_answer(user_answer, correct_answer)
    score = 0
    total_correct = 0
    # store user data in db
    if check:
        iscorrect = 'correct'
        total_correct += 1
        score = get_Score(question)
        quiz.add_entry(question, user_answer, iscorrect, score)
        return score, total_correct

    else:
        iscorrect = 'incorrect'
        quiz.add_entry(question, user_answer, iscorrect, score)
        return score, total_correct


def display_choices(question):
    """ display possible choices, shuffled """
    answers = quiz.get_possible_answers(question)
    return ui.show_choice(answers)


def display_points_available(question):
    """ display the ponts available for a question """
    points = quiz.get_possible_points(question)
    return points


def display_range(question):
    """ display the difficulty range for a question """
    difficulty_range = quiz.get_range(question)
    return difficulty_range


def display_answer(question):
    """ display the correct answer for a question """
    correct = quiz.get_answer(question)
    return correct


def get_Score(question):
    """ display the sum of the points """
    score = quiz.get_score(question)
    return score


main()
