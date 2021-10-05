import sqlite3
import os
import db_script
from db_script import Quize_Table
import datetime
result_db = db_script.db


# class Quiz_Result:
#     def __init__(self, category, iscorrect, useranswer, score):
#         self.category = category
#         self.iscorrect = iscorrect
#         self.useranswer = useranswer
#         self.score = score
#     self.quiz = Quize_Table()

# def create_result(self):
#     """ create a result table"""
#     create_sql = """ CREATE TABLE quiz_result (
#         id INTEGER PRIMARY KEY NOT NULL,
#         timestampstart DEFAULT CURRENT_TIMESTAMP,
#         timestampend DEFAULT CURRENT_TIMESTAMP,
#         category TEXT NOT NULL,
#         iscorrect TEXT NOT NULL,
#         useranswer TEXT NOT NULL,
#         total_score INT NOT NULL,
#         user_id INT NOT NULL,
#         FOREIGN KEY(user_id) REFERENCES quiz_questions(id))"""
#     conn = sqlite3.connect(result_db, detect_types=sqlite3.PARSE_DECLTYPES |
#                            sqlite3.PARSE_COLNAMES)  # returns cursor object
#     with conn:
#         conn.execute(create_sql)
#     conn.close()

# def add_entry(self, record):
#      "Add user result to the table"
#       insert_sql = 'INSERT INTO quiz_result (category,useranswer,score,iscorrect) VALUES(?,?,?,?)'

#        try:
#             with sqlite3.connect(result_db) as con:
#                 res = con.execute(insert_sql(
#                     record.category, record.iscorrect, record.useranswer, record.score))
#                 return res
#         except sqlite3.InterfaceError as e:
#             print(e)
#         finally:
#             con.close()
