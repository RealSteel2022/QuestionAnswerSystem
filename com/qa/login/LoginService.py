from tkinter import *  # importing tkinter
import hashlib


def register_user():
    username_info = username.get()  # takes the username
    password_info = password.get()  # takes the password

    passwordHashed = hashlib.md5(password_info.encode()).hexdigest()
    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(passwordHashed)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Information stored", fg="green", font=("calibri", 11), bg="SkyBlue2").pack()


def register():  # defines register so I can call it later
    global screen1
    screen1 = Toplevel(screen)  # brings the next screen over the main login screen
    screen1.title("Register")  # gives a title to the registry screen
    screen1.geometry("300x250")  # defines the dimensions of the next screen
    screen1['bg'] = "SkyBlue2"
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    # everything in this block below on screen1 or it will go on the other screen
    Label(screen1, text="Please enter details below", bg="SkyBlue2").pack()
    Label(screen1, text="", bg="SkyBlue2").pack()
    Label(screen1, text="Username", bg="SkyBlue2").pack()
    username_entry = Entry(screen1, textvariable=username, width=13)
    username_entry.pack()
    Label(screen1, text="Password", bg="SkyBlue2").pack()
    password_entry = Entry(screen1, textvariable=password, width=13)
    password_entry.pack()
    Label(screen1, text="", bg="SkyBlue2").pack()
    Button(screen1, text="Register", width=7, height=1, bg="SlateBlue1", activebackground="SlateBlue4",
           command=register_user).pack()


def login():
    print("Login session started")


def mainLogin_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen['bg'] = "SkyBlue2"
    screen.title("Revision Program")
    Label(text="Login System", bg="white", width="300", height="2", font=("Callibri", 13)).pack()
    Label(text="", bg="SkyBlue2").pack()
    Button(text="Login", height="2", width="30", bg="SlateBlue1", activebackground="SlateBlue4", command=login).pack()
    Label(text="", bg="SkyBlue2").pack()
    Button(text="Register", height="2", width="30", bg="SlateBlue1", activebackground="SlateBlue4",
           command=register).pack()


mainLogin_screen()
