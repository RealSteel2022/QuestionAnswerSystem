from tkinter import *

# Background/window below


def initial_menu():
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

    # Register button below

    def register_btn_clicked():
        print("Register Clicked")
        from MenuUI.RegisterInformation.RegisterWindow import register_window
        register_window()

    img0 = PhotoImage(file=f"img0.png")
    register_b = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=register_btn_clicked,
        relief="flat")

    register_b.place(
        x=160, y=700,
        width=241,
        height=64)

    # Login button below

    def login_btn_clicked():
        print("Login Clicked")

    img1 = PhotoImage(file=f"img1.png")
    login_b = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=login_btn_clicked,
        relief="flat")

    login_b.place(
        x=160, y=604,
        width=241,
        height=64)

    window1.resizable(False, False)
    window1.mainloop()


initial_menu()
