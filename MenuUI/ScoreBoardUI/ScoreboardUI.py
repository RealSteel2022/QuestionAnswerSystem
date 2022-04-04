from tkinter import *
import os

from com.qa.system.ScoreService import leaderboard_score

directory_path = str(os.getcwd()) + "\MenuUI\ScoreBoardUI\\"


def take_name_for_scoreboard():
    global current_user
    name = open("current_user.txt", "r")
    current_user = name.readlines()


def high_score_for_scoreboard():
    global current_high_score
    high_score = open("high_score.txt", "r")
    current_high_score = high_score.readlines()


global current_high_score
global current_user

take_name_for_scoreboard()
leaderboard_score()
# high_score_for_scoreboard()


def btn_clicked():
    window.destroy()
    from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window


window = Tk()

window.geometry("1139x794")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=794,
    width=1139,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=directory_path + "background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

img0 = PhotoImage(file=directory_path + "img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=926, y=707,
    width=187,
    height=65)

canvas.create_text(
    447.0, 297.5,
    text="Questions Correct: " + str(leaderboard_score()),
    fill="#737373",
    font=("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    569.0, 547.5,
    text="Keep going lets get a few more sessions in",
    fill="#737373",
    font=("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    422.0, 590.5,
    text="to round off the day.",
    fill="#737373",
    font=("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    570.0, 190.5,
    text="Well done " + current_user[0] + " here is your score",
    fill="#737373",
    font=("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    386.0, 404.5,
    text="High-score: ", # + current_high_score[0],
    fill="#737373",
    font=("Eczar-SemiBold", int(24.0)))

window.resizable(False, False)
window.mainloop()
