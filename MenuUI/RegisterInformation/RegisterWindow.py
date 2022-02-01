from tkinter import *

# Forming the main background

window = Toplevel()
window.geometry("562x794")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=794,
    width=562,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/RegisterInformation"
                                 "/RegisterBackground.png")
background = canvas.create_image(
    281.0, 397.0,
    image=background_img)

canvas.create_text(
    222.5, 691.0,
    text="Password",
    fill="#737373",
    font=("Spartan-Regular", int(24.0)))

canvas.create_text(
    222.5, 571.0,
    text="Username",
    fill="#737373",
    font=("Spartan-Regular", int(24.0)))

# allows entry to take in data

stored_username = StringVar()
stored_password = StringVar()

# user info button

img0 = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/RegisterInformation"
                       "/RegisterButton.png")
user_info_b = Entry(
    window,
    bg="#fff1a5",
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    textvariable=stored_username,
    highlightthickness=0,
    relief="flat")

user_info_b.place(
    x=160, y=586,
    width=241,
    height=64)

# password info button

img1 = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/RegisterInformation"
                       "/PasswordButton.png")
pass_info_b = Entry(
    window,
    bg="#fff1a5",
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    textvariable=stored_password,
    highlightthickness=0,
    relief="flat")

pass_info_b.place(
    x=160, y=702,
    width=241,
    height=64)


# ================ TEMPORARILY DISABLED TO REMOVE CLUTTERING =============================
# def storing_information():
#     import hashlib
#     print("Input accepted")
#     username_info = stored_username.get()  # takes the username
#     password_info = stored_password.get()  # takes the password
#
#     password_hashed = hashlib.md5(password_info.encode()).hexdigest()
#     file = open(username_info + ".txt", "w")
#     file.write(username_info + "\n")
#     file.write(password_hashed)
#     file.close()
#
#     user_info_b.delete(0, END)
#     pass_info_b.delete(0, END)

# tells the program what to do with accepted data

def accept_btn_clicked():
    print(stored_username.get())
    print(stored_password.get())
    # storing_information()


# accepting button to tell the program to store the data

img2 = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/RegisterInformation"
                       "/AcceptInput.png")
accept_b = Button(
    window,
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=accept_btn_clicked,
    relief="flat")

accept_b.place(
    x=481, y=734,
    width=64,
    height=32)

window.resizable(False, False)


# runs the window

def register_window():
    window.mainloop()


# register_window() only uncomment if testing in isolation
