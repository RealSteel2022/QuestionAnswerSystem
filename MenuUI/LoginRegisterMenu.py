import os
from tkinter import *

from MenuUI.ValidationCode import login_validation

username_info = ""


def greet_user():
    return username_info


# tells the register button what it does

def register_btn_clicked():
    from MenuUI.RegisterInformation.RegisterWindow import register_window
    register_window()


def send_details_clicked():
    login_validation(attempt_username.get(), attempt_password.get())
    clear_entry()
    if login_validation:
        window1.destroy()
        from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window


def clear_entry():
    username_entry_button.delete(0, END)
    password_entry_button.delete(0, END)


# initial menu

window1 = Tk()

window1.geometry("1139x794")
window1.configure(bg="#ffffff")
canvas = Canvas(
    window1,
    bg="#ffffff",
    height=794,
    width=1139,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=str(os.getcwd()) + "\MenuUI\\background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

# user attempts to log in

attempt_username = StringVar()
attempt_password = StringVar()

# user details entry button

sendDetails = PhotoImage(file=str(os.getcwd()) + "\MenuUI\img0.png")
sendDetails_button = Button(
    image=sendDetails,
    borderwidth=0,
    highlightthickness=0,
    command=send_details_clicked,
    relief="flat")

sendDetails_button.place(
    x=231, y=740,
    width=99,
    height=46)

# open register button

img1 = PhotoImage(file=str(os.getcwd()) + "\MenuUI\img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=register_btn_clicked,
    relief="flat")

b1.place(
    x=460, y=740,
    width=94,
    height=46)

canvas.create_text(
    230.5, 664.0,
    text="Password",
    fill="#737373",
    font=("Spartan-Regular", int(24.0)))

# username entry
username_entry = PhotoImage(file=str(os.getcwd()) + "\MenuUI\img2.png")

username_entry_button = Entry(
    bg="#fff1a5",
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    textvariable=attempt_username,
    highlightthickness=0,
    relief="flat")

username_entry_button.place(
    x=168, y=582,
    width=237,
    height=47)

# password entry

password_entry = PhotoImage(file=str(os.getcwd()) + "\MenuUI\img3.png")
password_entry_button = Entry(
    bg="#fff1a5",
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    show="*",
    textvariable=attempt_password,
    highlightthickness=0,
    relief="flat")

password_entry_button.place(
    x=168, y=675,
    width=237,
    height=47)

canvas.create_text(
    234.5, 571.0,
    text="Username",
    fill="#737373",
    font=("Spartan-Regular", int(24.0)))

window1.resizable(False, False)


def login_register_menu():
    window1.mainloop()
