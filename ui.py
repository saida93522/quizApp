from db_script import Quize_Table
"This module gets data from the db and displays to the user questions and their score"
quiz = Quize_Table()


def welcome_banner():
    """ Print a message to the user"""
    print('\tPut your knowledge to the test with this Ultimate Quiz Questions!')
    print('----The Rules are simple------')
    print('There are 3 topics available: Art, Space, Sport')
    print('Choose a topic and number of question you would like to attempt between(1-5)')
    print('Enter "q" to quit the game')


def show_question(questions):
    """ Display all of the available question"""
    # for question in questions:
    #     return question

    # correct = quiz.get_answer(question)
    # user_answer = input('Enter here: ').lower()
    # if user_answer in correct.lower():
    #     print('Corret\n')
    #     score += 1
    # else:
    #     print(
    #         f'sorry that was incorrect, the corect answer is {correct}\n')


def show_choice(answers):
    # for answer in answers:
    print('')


def get_answer(question):
    """ get user response"""
    return input(question)

# 1. displays the available topics to the user and num of question available for that topic.
# - display category and num of question for that category
# - that reads quiz question from the database,
# - return result to the quiz result class
# --CRUD

# 2. class that verifies what the user entered is correct and returns the result

# 3. class that creates and stores quiz result


# print(result.display_category())
