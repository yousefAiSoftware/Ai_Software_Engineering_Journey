import random
print("Welcome to our guess game ")
print("You have to Guess 2 numbers from [1 ~ 5] out of 3 trials")
nums= [1,2,3,4,5]
computer_num = random.choice(nums)
trials = 0
correct = 0
def game(trials , correct):
    global computer_num
    if trials < 3 :
        player_guess = int(input("Enter your guessed number : "))
        trials +=1
        print(f"you are now in trial num :  {trials}")
        if player_guess == computer_num :            
            correct+=1
            print(f"You guessed correct Num it was : {player_guess}")
            if correct == 2 :
                print("Congratulations, You Win ! ")
                quit()
            computer_num = random.choice(nums)
            game(trials,correct)
        else:
            print("TryAgain~~~")
            game(trials,correct)
    else :
        print("You Finished your all trails, See you Again~~~")
        quit()




game(trials,correct)