import random
import time
import math
"This module gets data from the db and displays to the user questions and their score"


def welcome_banner():
    """ Print a message to the user"""
    print('\tPut your knowledge to the test with this Ultimate Quiz Questions!')
    print('----The Rules are simple------')
    # The choice of topics should come from the data availale in the database, not coded into the program 
    print('There are 3 topics available: Art, Space, Sport')
    print('Choose a topic and number of question you would like to attempt between(1-5)')
    print('Enter "quit" to quit the game')


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


def check_user_answer(user_answer, correct_answer):
    # If I answer "Simone Biles" and the correct answer, in lowercase, is "simone biles" 
    # this will decide the answer is incorrect and return false.  So lowercase both user answer and correct answer. 
    if user_answer.lower() == correct_answer.lower():
        print('corret')
        return True
    else:
        print(
            f'sorry that was incorrect, the corect answer is {correct_answer}\n')
        return False

# this function also calculates time elapsed. That logic belongs in another function
# instead of stime, can this function have the total time as a parameter? 
def show_result(stime, questions, correct_answers, points_avbl, total_score):
    print('\n---Result---')
    print(
        f'The time taken to complete the quiz: {math.floor(time.time() - stime)} seconds')
    print(f'Number of questions asked: {questions}')
    print(f'Number of correct answers: {correct_answers}')
    print(f'Total points available: {points_avbl}')
    print(f'Total points earned: {total_score}')
    print(f'You got {(total_score/points_avbl) * 100}% questions right')
