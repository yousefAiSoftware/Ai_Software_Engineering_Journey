import random

def get_choices():
    player_choice = input("Enter your choice => paper , rock , scissor :")
    options = ["rock" , "paper" , "scissor"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer" : computer_choice}

    return choices

def check_win(player , computer):
    print (f"you chose : {player} , computer chose : {computer} ")
    
    if player == computer:
        result = "It's a tie!"
    elif player == "rock" :
        if computer == "scissor":
            result = "rock over scissor , You Win!"
        else :
            result = "paper over rock , You Lose~"
    elif player == "paper" :
        if computer == "rock" :
            result = "paper over rock , You Win!"
        else :
            result = "scissor cuts paper , You Lose~"
    else :
        if computer == "paper" :
            result = "scissor cut paper , You Win!"
        else :
            result = "Rock over scissor , You Lose~"

    return result


choices = get_choices()
final_result = check_win(choices["player"] , choices["computer"])
print(final_result)