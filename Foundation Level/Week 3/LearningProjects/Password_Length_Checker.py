print("Welcome to our password lenght checker app...")
while True:
    user_password = input("Enter the password : ")
    if len(user_password) >= 8:
        print("Password Accepted")
        break;
    print("Password is too short.")