from tkinter import *

username_info = ""


# ================ ALLOW USER TO LOG IN =============================

def login_validation():
    import hashlib
    global username_info
    username_info = attempt_username.get()  # takes the username
    password_info = attempt_password.get()  # takes the password

    password_hashed = hashlib.md5(password_info.encode()).hexdigest()  # compares hash value to stored data
    file = open(username_info + ".txt", "r")
    lines = file.readlines()
    if password_hashed == lines[1]:
        file = open("current_user.txt", "w")
        file.write(username_info)
        file.close()
        print(username_info)
        window1.destroy()
        from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window
    else:
        print("Incorrect Password")
        # need a display user incorrect password service
    file.close()

    username_entry_button.delete(0, END)
    password_entry_button.delete(0, END)


def greet_user():
    return username_info


# tells the register button what it does

def register_btn_clicked():
    from MenuUI.RegisterInformation.RegisterWindow import register_window
    register_window()


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

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

# user attempts to log in

attempt_username = StringVar()
attempt_password = StringVar()

# user details entry button

sendDetails = PhotoImage(file=f"img0.png")
sendDetails_button = Button(
    image=sendDetails,
    borderwidth=0,
    highlightthickness=0,
    command=login_validation,
    relief="flat")

sendDetails_button.place(
    x=231, y=740,
    width=99,
    height=46)

# open register button

img1 = PhotoImage(file=f"img1.png")
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
username_entry = PhotoImage(file="img2.png")

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

password_entry = PhotoImage(file=f"img3.png")
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
window1.mainloop()
