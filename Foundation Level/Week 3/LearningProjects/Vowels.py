print("Welcome to our Vowels App...")
user_input = list(input("Enter the sentence : ").lower())
Vowels = ["a","e","i","u","o"]
index = 0
for letter in user_input:
    if letter in Vowels:
        print(f"Found vowel letter '{letter}' at index '{index}' !")
        index+=1
        break;