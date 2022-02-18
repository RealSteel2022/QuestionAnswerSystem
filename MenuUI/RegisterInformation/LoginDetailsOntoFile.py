def storing_information(username_info, password_info):
    import hashlib
    password_hashed = hashlib.md5(password_info.encode()).hexdigest()
    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(password_hashed)
    file.close()