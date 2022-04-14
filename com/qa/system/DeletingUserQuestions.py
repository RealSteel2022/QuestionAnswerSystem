import sqlite3


def deleting_user_questions(stored_subject, stored_question):
    conn = sqlite3.connect('com\qa\system\questions.db')

    with conn:
        c = conn.cursor()

        deleting_sql = """DELETE FROM stored_questions WHERE
        (question)
        = ('{}');""".format(
            stored_question)

        c.execute(deleting_sql)

        c.execute("SELECT * FROM stored_questions")

        rows = c.fetchall()

        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}")
