''' Question and Answer '''
import time
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


# id, question, category, correct, wrong1, wrong2, wrong3, difficulty, points
#  self.id = id
#         self.question = question
#         self.category = category
#         self.correct = correct
#         self.wrong1 = wrong1
#         self.wrong2 = wrong2
#         self.wrong3 = wrong3
#         self.difficulty = difficulty
#         self.points = points


"""
Expected output:
Welcome to the ultimate trivia quiz question
----Here are the rule-------
There 3 topics available: Art, Space, Sport,
Each topic has 5 questions and you can earn up to 15 points.
choose a topic and number of question you would like to attempt(1-5)
Enter The Letter you belive points to the write answer.
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
Enter Letter: C

Correct! 

Q1) which planet his closest to the sun(difficulty:1)(worth 2 points)
    A.wrong2
    B.wrong1
    C.wrong3
    D.correct
Enter Letter: A

Unfortunetly that is incorrect
The correct answer is D Mercury

--Results--
Time took to complete the quiz: 3 minutes
Number of questions asked: 2
Number of correct answers: 1
Total points available: 5 
Total number of points earned: 3 
Percentage score [Percentage score = points earned / points available * 100 ]




create_sql = CREATE TABLE quiz_questions(
            id INTEGER PRIMARY KEY,
            questions TEXT,
            correct TEXT,
            wrong1 TEXT NOT NULL,
            wrong2 TEXT NOT NULL,
            wrong3 TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty INT,
            possible_points INT,
            timestampstart DEFAULT CURRENT_TIMESTAMP,
            UNIQUE( questions COLLATE NOCASE, correct COLLATE NOCASE))
//
restart game



"""
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
