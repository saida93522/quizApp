""" Program displays the available topics from the database as well as the number of questions for that topic. """
#!/usr/bin/env python

from db_script import Quize_Table
import ui
import valid as valid
import random
import sys
import time
quiz = Quize_Table()



def main():
    ui.welcome_banner()
    while True:
        # you don't need a loop here - play one quiz game each time the program runs 
        topic = valid.check_topic_input()
        if topic == 'quit':
            break
        else:
            display_questions(topic)
        


def display_questions(topic):
    """ displays list of questions 
    :param a tuple containing chosen topic and number of questions user wants to answer"""
    topic, num_questions = topic
    questions = quiz.get_questions(topic, num_questions)
    total_point_avbl = []  # avoid abbreviations in variable names. total_points_available is a better name 
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


def get_response(question):  # be more specific with function names.  ask_user_question_check_response maybe?
    """ get the user response and add data in quiz_result table  """
    user_answer = ui.ask_question('Enter your answer here: ')
    correct_answer = display_answer(question)
    # validate user entered correct answer
    check = ui.check_user_answer(user_answer, correct_answer)
    score = 0
    total_correct = 0
    # store user data in db
    if check:
        iscorrect = 'correct' # is_correct is a better name 
        total_correct += 1
        score = get_Score(question)  # be consistent with cases - get_score, lowercase S
        quiz.add_entry(question, user_answer, iscorrect, score)
        return score, total_correct

    else:
        iscorrect = 'incorrect'
        quiz.add_entry(question, user_answer, iscorrect, score)
        return score, total_correct


def display_choices(question):
    """ display possible choices, shuffled """
    answers = quiz.get_possible_answers(question)
    return ui.show_choice(answers)  # ui.show_choice prints the data, it doesn't return anything. 


def display_points_available(question):  
    """ display the ponts available for a question """
    points = quiz.get_possible_points(question)
    return points   


def display_range(question):  # does this display or get data from the database? is get_range a better name? 
    """ display the difficulty range for a question """
    difficulty_range = quiz.get_range(question)
    return difficulty_range


def display_answer(question): # does this display or get data from the database?  How about get_correct_answer ? 
    """ display the correct answer for a question """
    correct = quiz.get_answer(question)
    return correct


def get_Score(question): # function names - get_score 
    """ display the sum of the points """
    score = quiz.get_score(question)
    return score


main()
