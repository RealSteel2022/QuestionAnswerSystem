temporary_lb_score = 2
session_score = 0

# empties at start


def scored_point():
    global session_score
    global session_score_file
    print("point scored")
    session_score += 1
    print(session_score)
    session_score_file = open("session_score.txt", "w")
    session_score_file.write(str(session_score))
    session_score_file = open("session_score.txt", "r")
    lines = session_score_file.readlines()
    print(lines[0])
    session_score_file.close()


def clear_score():
    clearing_sessions_score = open("session_score.txt", "w")
    clearing_sessions_score.write("0")
    clearing_sessions_score.close()

def update_high_score():
    global session_score_file
    session_score_file = open("session_score.txt", "r")
    high_score_file = open("high_score.txt", "w")
    lines = session_score_file.readlines()
    high_score_file.write(str(lines[0]))
    high_score_file.close()
    session_score_file.close()


def leaderboard_score():
    session_score_file = open("session_score.txt", "r")
    lines = session_score_file.readlines()
    the_session_score = lines[0]
    print("inside thing " + the_session_score)
    high_score = open("high_score.txt", "r")
    read_high_score = high_score.readlines()
    high_score_from_file = read_high_score[0]
    if int(3) > int(2):
        print("New high-score of " + str(the_session_score))
        update_high_score()
    else:
        print("You were unable to beat your previous high-score of " + str(
            session_score_file) + " your session score was " + str(session_score_file))

# I've got the program running but it doesn't clear the score when ti starts need to try and add that in then
# configure the rest of the program to get it to look nicer and to present it onto the UI
