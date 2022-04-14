temporary_lb_score = 2
session_score = 0

# empties at start


def scored_point():
    global session_score
    print("point scored")
    session_score += 1
    print(session_score)


def update_high_score():
    pass


def leaderboard_score():
    if int(3) > int(2):
        print("New high-score of " + str(session_score))
        update_high_score()
    else:
        print("You were unable to beat your previous high-score of " + str(
            session_score) + " your session score was " + str(session_score))

# I've got the program running but it doesn't clear the score when ti starts need to try and add that in then
# configure the rest of the program to get it to look nicer and to present it onto the UI
