import sqlite3
import datetime
import os
import csv
# Path('database', 'quiz_records.db').touch()
db = os.path.join('database', 'quiz_records.db')


# class Quiz:
#     def __init__(self, chosen_category, num_of_questions):
#         self.chosen_category = chosen_category
#         self.num_of_questions = num_of_questions

#         self.quizz = Quize_Table()


class Quize_Table:
    """Singleton class that renders quize question from db creates,inserts and returns quiz questions.does not store anything from user"""
    instance = None

    def create_questions(self):
        """ create a question table,column matches csv file column heading """

        create_sql = """ CREATE TABLE quiz_questions(
            id INTEGER PRIMARY KEY,
            questions TEXT,
            correct TEXT,
            wrong1 TEXT NOT NULL,
            wrong2 TEXT NOT NULL,
            wrong3 TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty INT,
            possible_points INT,
            UNIQUE( questions COLLATE NOCASE, correct COLLATE NOCASE))"""

        conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES |
                               sqlite3.PARSE_COLNAMES)  # returns cursor object
        with conn:
            conn.execute(create_sql)
        conn.close()

    def insert_questions(self):
        """ open csv file that contains quiz data and insert them into the table """
        conn = sqlite3.connect(db)

        # won't affect application size much
        key_file = 'database/key.csv'
        with open(key_file, newline='') as filr:
            reader = csv.DictReader(filr)
            add_rows = [(i['questions'], i['correct'], i['wrong1'], i['wrong2'], i['wrong3'],
                         i['category'], i['difficulty'], i['possible_points']) for i in reader]  # loop through csv col
        conn.executemany(
            "INSERT INTO quiz_questions('questions','correct','wrong1','wrong2','wrong3','category','difficulty','possible_points') VALUES (?,?,?,?,?,?,?,?)", add_rows)  # add to table
        conn.commit()
        conn.close()

    def display_category(self):
        """ :returns all available topics """

        select_sql = 'SELECT DISTINCT category  FROM quiz_questions'

        conn = sqlite3.connect(db)
        topic = conn.execute(select_sql)
        conn.row_factory = sqlite3.Row
        total = topic.fetchall()
        topics = []
        for i in total:
            topics.append(i[0])

        conn.close()
        # print(topics)
        return topics

    def get_questions(self, chosen_category, num_of_questions):
        """ Get a list of questions based on chosen topic
        :param topic to choose the category to fnd the questions, num_of_questions to Limit number of questions returned
        :returns list of questions based given topic
        """

        art_sql = 'SELECT rowid, questions FROM quiz_questions WHERE category = ? LIMIT ?'

        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rows = c.execute(art_sql, (chosen_category, num_of_questions))
        # total = [tup for tup in c.fetchall()]
        total = []
        for r in rows:
            q = r['questions']
            total.append(q)

        c.close()
        return total

    def get_question_count(self, topic):
        """:return total number of questions for one category"""
        # topic = self.display_category()
        points_sql = 'SELECT COUNT(questions) FROM quiz_questions WHERE category = ?'

        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        # count = []
        topic = c.execute(points_sql, (topic,)).fetchone()[0]
        # for row in topic:
        #     points = c.execute(points_sql, (row,)).fetchone()[0]
        #     count.append(points)

        # points = c.fetchone()
        c.close()
        return topic

    def get_possible_answers(self, question):
        """ Get a list of possible answers based on given topic
        :param topic to choose the category to fnd the answers, num_of_questions to Limit number of possible answers returned
        :returns list of possible answers based given topic question
        """
        # try = [e for t in chosen_category for e in t]
        # list_format = ','.join(try)

        options_sql = 'SELECT correct, wrong1, wrong2, wrong3 FROM quiz_questions WHERE questions = ?'

        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        rows = c.execute(options_sql, (question,)).fetchone()
        options = []
        for r in rows:
            options.append(r)

        c.close()
        return options

    def get_answer(self, question):
        "get answer"
        correct_sql = 'SELECT correct FROM quiz_questions WHERE questions = ?'
        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        rows = c.execute(correct_sql, (question,)).fetchone()[0]
        c.close()
        return rows

    def get_possible_points(self, question):
        """" Get a possible number of points
        :param list of question based on chosen catergory, num_of_questions user wants to attempt"""
        points_sql = 'SELECT possible_points FROM quiz_questions WHERE questions = ? '

        # topic = self.display_category()
        # print(topic)

        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        rows = c.execute(points_sql, (question,)).fetchone()[0]

        # count = []
        # for row in rows:
        #     points = row['possible_points']
        #     count.append(points)
        c.close()
        return rows

    def get_range(self, questions):
        """ Get a difficulty"""
        range_sql = 'SELECT difficulty FROM quiz_questions WHERE questions = ? '

        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        rows = c.execute(range_sql, (questions,)).fetchone()[0]

        # for row in rows:
        #     points = row['difficulty']
        #     count.append(points)
        c.close()
        return rows

    def get_score(self, question):
        """:return total number of questions for one category"""
        points_sql = 'SELECT SUM(possible_points) FROM quiz_questions WHERE questions = ?'
        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        # count = []
        topic = c.execute(points_sql, (question,)).fetchone()[0]

        c.close()
        return topic

    def get_timestamp(self):
        pass

    def add_entry(self, topic, user_answer, score, iscorrect):
        "Add user result to the table"
        insert_sql = 'INSERT INTO quiz_result (category,useranswer,total_score,iscorrect) VALUES(?,?,?,?)'
        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        c = c.cursor()
        res = c.execute(insert_sql, (topic, user_answer, score, iscorrect))

        c.close()
        return res

# result = Quize_Table()
# r = result.get_score('Which planet has the fastest rotation?')
# print(r)


class QuizError(Exception):
    pass
