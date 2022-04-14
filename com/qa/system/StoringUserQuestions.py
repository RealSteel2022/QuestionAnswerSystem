import sqlite3


def storing_user_questions(stored_subject, stored_question, stored_answer):
    conn = sqlite3.connect('com\qa\system\questions.db')

    with conn:
        c = conn.cursor()
        #
        # c.execute("""CREATE TABLE stored_questions (
        #             question text,
        #             answer text,
        #             subject text
        #             )""")

        executing_sql = """INSERT INTO stored_questions 
        (question, answer, subject)
        VALUES ('{}', '{}', '{}');""".format(
            stored_question, stored_answer, stored_subject)

        c.execute(executing_sql)

        c.execute("SELECT * FROM stored_questions")

        rows = c.fetchall()

        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}")
