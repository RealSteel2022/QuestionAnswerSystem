from com.qa.system import SessionScoreAccumulator

temporary_lb_score = 2
session_score = 0

# empties at start


def scored_point():
    # global session_score
    # global SessionScoreAccumulator.session_score_accumulator
    print("point scored")
    # session_score += 1
    # return session_score


def update_high_score():
    pass


def leaderboard_score():
    if int(3) > int(2):
        print("New high-score of " + "3")
        update_high_score()
    else:
        print("You were unable to beat your previous high-score of " + "3" + " your session score was "
              + "2")
        # SessionScoreAccumulator.initialize()

# I've got the program running but it doesn't clear the score when ti starts need to try and add that in then
# configure the rest of the program to get it to look nicer and to present it onto the UI
