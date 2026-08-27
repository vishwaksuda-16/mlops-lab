def login(username, password):
    if username.strip() == "admin" and password == "admin123":
        return "User authenticated successfully"
    return "Invalid credentials"


print(login("admin", "admin123"))
