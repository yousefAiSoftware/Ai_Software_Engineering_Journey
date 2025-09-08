print("Welcome to our square num code...")
user_num = int(input("Enter the num {0 - 20} : "))
def game(user_num):
    if user_num in range(0 , 21):
        for i in range(0,user_num):
            print(i**2)
    else:
        print("Out OF Range")
game(user_num)