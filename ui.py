import random
import time
import math
"This module gets data from the db and displays to the user questions and their score"


def welcome_banner():
    """ Print a message to the user"""
    print('\tPut your knowledge to the test with this Ultimate Quiz Questions!')
    print('----The Rules are simple------')
    print('There are 3 topics available: Art, Space, Sport')
    print('Choose a topic and number of question you would like to attempt between(1-5)')
    print('Enter "q" to quit the game')


def show_question(question, difficulty, points):
    """ display question """
    return print(f'{question} difficulty-range ({difficulty}/5) worth ({points}) points')


def show_choice(answers):
    """ shuffle answer choices """
    random.shuffle(answers)
    for answer in answers:
        choice_list = (f'\t*{answer}')
        print(choice_list)


def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)


def show_result(stime, questions, correct_answers, points_avbl, total_score):
    print('\n---Result---')
    print(
        f'The time taken to complete the quiz: {math.floor(time.time() - stime)} seconds')
    print(f'Number of questions asked: {questions}')
    print(f'Number of correct answers: {correct_answers}')
    print(f'Total points available: {points_avbl}')
    print(f'Total points earned: {total_score}')
    print(f'You got {(total_score/points_avbl) * 100}% questions right')


# 1. displays the available topics to the user and num of question available for that topic.
# - display category and num of question for that category
# - that reads quiz question from the database,
# - return result to the quiz result class
# --CRUD
