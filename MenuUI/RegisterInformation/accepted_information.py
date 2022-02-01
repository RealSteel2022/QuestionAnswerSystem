# def accept_btn_clicked():
#     print("Input accepted")
#     username_info = username.get()  # takes the username
#     password_info = password.get()  # takes the password
#
#     password_hashed = hashlib.md5(password_info.encode()).hexdigest()
#     file = open(username_info + ".txt", "w")
#     file.write(username_info + "\n")
#     file.write(password_hashed)
#     file.close()
#
#     username_entry.delete(0, END)
#     password_entry.delete(0, END)