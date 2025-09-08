print("Welcome to our HANGMAN Game....!")
password = "apple"
password_letters = list(password)
attempts = len(password_letters) + 5
lives = 5
current_index = 0
print("We have created a new password, Guess letters...")
player_list = ["_","_","_","_","_"]
print(player_list)
def game(current_index, player_list,):
    global attempts
    global lives
    
    user_input = input("Enter the letter : ")
    attempts -=1
    if attempts != 0 and lives != 0:
        if user_input in password_letters:
            print(f"It's Correct , the word has {user_input}")
            check(player_list,current_index,user_input)
            print(player_list)
            if player_list == password_letters:
                print("Congratulations, you guessed the word correctly and saved the man life")
                quit()
            game(current_index,player_list)
        else:
            lives-= 1
            print("It's wrong, TryAgain~0")
            game(current_index,player_list)
    else:
        print("You have finished your Trials")
        quit()

        


def check(player_list, current_index,user_input):
    if current_index < len(player_list):
        if user_input != password_letters[current_index]:
            current_index+=1
            check(player_list,current_index,user_input)
        else:
            player_list[current_index] = password_letters[current_index]
            current_index+=1
            check(player_list,current_index,user_input)
    return player_list


game(current_index,player_list)