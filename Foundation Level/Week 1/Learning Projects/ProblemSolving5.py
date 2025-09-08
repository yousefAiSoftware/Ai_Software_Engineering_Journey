import random
print("Welcome to our Guess Ordered Game....!")
original_word = input("Enter the word : ")
word_letters = list(original_word)
current_index = 0
failed_attempts = 0
ordered_ltters =random.sample(word_letters,len(word_letters))
ordered_word = "".join(ordered_ltters)
print("Now, we re-ordered the letters for your word, you hve to guess new word letter-by-letter")

def game(current_index , failed_attempts ):
    global ordered_ltters
    global ordered_word
    user_input = input(f"Enter the letter {current_index+1} : ")
    if user_input == ordered_ltters[current_index]:
        print(f"you are right the letter {current_index+1} is : {user_input}")
        current_index+=1
        failed_attempts = 0
        if current_index == len(ordered_ltters):
            print(f"Congratulations, you guessed the word it was : {ordered_word}")
            quit()
        else:
            game(current_index, failed_attempts)
    else:
        print("It's Wrong, TryAgain")
        failed_attempts+=1
        if failed_attempts ==2:
            ordered_ltters = random.sample(word_letters,len(word_letters))
            ordered_word = "".join(ordered_ltters)
            print("You have entered 2 failed attempts, so, we're re-ordered the word, TryAgain")
            current_index = 0
            failed_attempts = 0
            game(current_index, failed_attempts)
        else:
            game(current_index, failed_attempts)
game(current_index, failed_attempts)