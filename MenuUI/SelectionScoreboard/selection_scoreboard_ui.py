import os
from tkinter import *

directory_path = str(os.getcwd()) + "\MenuUI\SelectionScoreboard\\"

def btn_clicked():
    window.destroy()
    from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window


window = Tk()

window.geometry("1139x794")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 794,
    width = 1139,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file =directory_path + "background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

img0 = PhotoImage(file =directory_path + "img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 926, y = 707,
    width = 187,
    height = 65)

canvas.create_text(
    410.5, 562.5,
    text = "Total time spent: ",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    415.0, 476.5,
    text = "Points on subject:",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    427.0, 390.5,
    text = "Most recent subject:",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    672.0, 390.5,
    text = "(Subject)",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    667.0, 476.5,
    text = "(Points)",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

canvas.create_text(
    693.5, 562.5,
    text = "(Time spent)",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

window.resizable(False, False)
window.mainloop()
