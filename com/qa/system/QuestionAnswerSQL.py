import sqlite3

conn = sqlite3.connect('questions.db')

with conn:
    c = conn.cursor()

    # c.execute("""CREATE TABLE stored_questions (
    #             question text,
    #             answer text,
    #             subject text
    #             )""")

    # c.execute("""CREATE TABLE user_high_score (
    #             score_key int,
    #             user text,
    #             high_score int
    #             )""")


    # c.execute("INSERT INTO stored_questions VALUES ('How big was Henry VIII privy council?', '12 members', 'History')")

    c.execute("SELECT * FROM stored_questions")

    print(c.fetchall())

    c.execute("SELECT * FROM stored_questions")

    rows = c.fetchall()

    for row in rows:
        print(f"{row[0]} {row[1]}")

    # conn.commit()
    #
    # conn.close()
