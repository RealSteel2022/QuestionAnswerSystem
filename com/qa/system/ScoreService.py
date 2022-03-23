temporary_lb_score = 2
session_score = 0


def scored_point():
    global session_score
    print("point scored")
    session_score += 1
    print(session_score)
    session_score_file = open("session_score.txt", "w")
    session_score_file.write(str(session_score))
    session_score_file.close()


def update_high_score():
    session_score_file = open("session_score.txt", "w")
    high_score_file = open("high_score.txt", "w")
    high_score_file.write(str(session_score_file))
    high_score_file.close()
    session_score_file.close()
    new_high_score = True


def leaderboard_score():
    score = open("session_score.txt", "r")
    lines = score.readlines()
    score_from_file = lines[0]
    high_score = open("session_score.txt", "r")
    high_score_lines = high_score.readlines()
    high_score_from_file = high_score_lines[0]
    if int(score_from_file) > int(high_score_from_file):
        print("New high-score of " + str(high_score_from_file))
        update_high_score()
    else:
        print("You were unable to beat your previous high-score of " + str(temporary_lb_score) + "your session score was " + str(score_from_file))
        print(score_from_file)
        new_high_score = False
