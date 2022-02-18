
def login_validation(username_info, password_info):
    import hashlib
    password_hashed = hashlib.md5(password_info.encode()).hexdigest()  # compares hash value to stored data
    file = open(username_info + ".txt", "r")
    lines = file.readlines()
    if password_hashed == lines[1]:
        file = open("current_user.txt", "w")
        file.write(username_info)
        file.close()
        return True
    else:
        print("Incorrect Password")
        # need a display user incorrect password service
    file.close()
