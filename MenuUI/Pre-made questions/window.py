from tkinter import *


def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file =f"background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

img0 = PhotoImage(file =f"img0.png")
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
    569.5, 259.5,
    text = "Pick a subject below",
    fill = "#737373",
    font = ("Eczar-SemiBold", int(24.0)))

img1 = PhotoImage(file =f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 496, y = 561,
    width = 147,
    height = 50)

img2 = PhotoImage(file =f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 381, y = 308,
    width = 155,
    height = 45)

img3 = PhotoImage(file =f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 381, y = 394,
    width = 155,
    height = 45)

img4 = PhotoImage(file =f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 602, y = 477,
    width = 155,
    height = 45)

img5 = PhotoImage(file =f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 381, y = 477,
    width = 155,
    height = 45)

img6 = PhotoImage(file =f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 602, y = 394,
    width = 155,
    height = 45)

img7 = PhotoImage(file =f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 602, y = 309,
    width = 155,
    height = 45)

window.resizable(False, False)
window.mainloop()
