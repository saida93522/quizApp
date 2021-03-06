''' Question and Answer '''
# start sample questions
questions = {
    'art': {
        'Who painted the Mona Lisa?\t': 'Leonardo da Vinci',
        'What precious stone is used to make the artist\'s pigment ultramarine?\t': 'Lapiz lazuli',
        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?\t': 'Chicago'
    },

    'space': {
        'Which planet is closest to the sun?\t': 'Mercury',
        'Which planet spins in the opposite direction to all the others in the solar system?\t': 'Venus',
        'How many moons does Mars have?\t': '2'
    },
    'sport': {
        'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after? \t': 'Simone Biles',
    }
}

#  An instance is a specific object created from a particular class.
# class variables are, variables that are shared among all instances of a class

# 1. displays the available topics to the user and num of question available for that topic.
# - display category and num of question for that category
# - that reads quiz question from the database,
# - return result to the quiz result class
# --CRUD


"""
Expected output:
Welcome to the ultimate trivia quiz question
----Here are the rule-------
There 3 topics available: Art, Space, Sport,
Each topic has 5 questions and you can earn up to 15 points.
choose a topic and number of question you would like to attempt(1-5)
also difficult range(on a 1-5 scale. 1 is easiest, 5 is hardest.) will be displayed next to each question
-----
Enter Topic(art,space,sport): space
Enter Number of questions you would like to attempt(1-5): 2

--Chosen Topic: Space  Number of questions: 2
Q1) which planet has the fast rotation(difficulty:2)(worth 3 points)
    A.wrong2
    B.wrong1
    C.correct
    D.wrong3
Enter answer: 

Correct! 

Q1) which planet his closest to the sun(difficulty:1)(worth 2 points)
    A.wrong2
    B.wrong1
    C.wrong3
    D.correct
Enter answer: 

Unfortunetly that is incorrect
The correct answer is Mercury

--Results--
Time took to complete the quiz: 3 minutes
Number of questions asked: 2
Number of correct answers: 1
Total points available: 5 
Total number of points earned: 3 
Percentage score [Percentage score = points earned / points available * 100 ]




//
restart game



"""
