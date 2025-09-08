print("Welcome To Our Guess letters from dintict word game !!!")
password = "yousefpthn"
password_letters = list(password)
user_letters = []
def game():
    if set(user_letters) == set(password_letters):
        print(f"Congratulations, You guessed all letters in thw word it was : {password}")
        quit()
    else:
        user_input = input("Enter the letter : ")
        if user_input in password_letters:
            if user_input not in user_letters:
                user_letters.append(user_input)
                print(f"Correct, the word has : {user_input}")
                print(f"your correct letters : {user_letters}")
                game()
            else:
                print(f" [{user_input}] => is already in {user_letters}")
                game()
        else:
            print("TryAgain~~~")
            game()
game()