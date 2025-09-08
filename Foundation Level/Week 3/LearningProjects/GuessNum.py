import random
def game():
    print("Welcome To our Guess Game...")
    computer_num = random.randint(0,100)
    print("We Choosed num (0 - 100), you have to guess it within 10 trials to win...")
    trails = 10
    while trails > 0:
        print(f"Your trails is : {trails}")
        user_num = int(input("Enter The num : "))
        trails-=1
        if user_num != computer_num:
            print("Wrong Num~")
            if user_num > computer_num:
                print(f"The num is less than {user_num}")
            else:
                print(f"The num is Greater than {user_num}")
        else:
            print(f"Congratulations, You guessed it was : {computer_num} = {user_num}")
            break;
    else:
        print(f"You finished your all trails, the num was : {computer_num},  TryAgain")
game()