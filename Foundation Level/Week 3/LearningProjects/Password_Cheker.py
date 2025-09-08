print("This is Password Cheker App....")
def outer():
    passwords = []
    def user_password():
        new_password = input("Enter the new password : ")
        if new_password not in passwords:
            print(f"Your Password : <{new_password}> has been saved")
            passwords.append(new_password)
        else:
            print("Your password is already used before.")
        ask = input("Do you want to change your password ? (y/n) : ").lower()
        if ask == "y":
            user_password()
        elif ask == "n":
            quit()
        else:
            print("Invalid Value! TRYAGAIN~~~")
            quit()
    return user_password

passwords = outer()
passwords()