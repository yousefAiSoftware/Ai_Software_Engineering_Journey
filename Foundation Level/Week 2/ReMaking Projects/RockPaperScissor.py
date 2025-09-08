import random
print("Welcome to our game Rock, Paper, Scissor")
choices = ["rock", "paper", "scissor"]
def computer_random():
    computer_choice = random.choice(choices)
    return computer_choice
def game():
    user_choice = input("Enter your choice (rock , paper , scissor) : ")
    computer_random()
    if user_choice == computer_random() :
        print("It's tie")
    elif user_choice == "rock":
        if computer_random() == "scissor":
            print("Rock over Scissor, You Win!")
        else:
            print("Paper over Rock, You Lose~~~")
    elif user_choice == "paper":
        if computer_random() == "rock":
            print("Paper over Rock, You Win!")
        else:
            print("Scissor cuts Paper, You Lose~~~")
    elif user_choice == "scissor":
        if computer_random() == "paper":
            print("Scissor cuts Paper, You Win!")
        else:
            print("Rock over Scissor, You Lose~~~")
    agian()

def agian():
    ask = input("Do you want to play again ? (y/n) : ")
    if ask == "y":
        game()
    elif ask == "n":
        quit()
    else:
        print("Invalid Value ! , Try Again")
        agian()

game()


