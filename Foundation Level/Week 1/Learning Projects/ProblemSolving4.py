print("Hello Today...")
print("Our game to guess a letter from a static word")

word = "yousef"
word_letters = list(word)
print("We choose a word , you have to guess the all dintict letters in this word ")
user_letters = []
def check():
    user_input = input("Enter the letter : ")
    if  user_input in  word:
        print (f"Correct, the word has {user_input}")
        storing(user_input)
    else:
        print("Try Again")
        check()
    return user_input
        

def storing (user):
    user_letters.append(user)
    if set(user_letters) == set(word_letters):
        print("Congratulations, You guessed all letters in the word")
        print(f"The word was : {word}")
    else:
        check()

check()
