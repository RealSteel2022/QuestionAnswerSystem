temporary_lb_score = 2
session_score = 0


def scored_point():
    global session_score
    session_score += 1


def leaderboard_score():
    if session_score > temporary_lb_score:
        print("New high-score of " + str(session_score))
    else:
        print("You were unable to beat your previous high-score of " + str(temporary_lb_score))
