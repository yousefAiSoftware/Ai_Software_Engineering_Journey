import random
print("Welcome to our ordered guess game !!!")
original_word = input("Enter the word you want to order : ")
original_word_letters = list(original_word)
random.shuffle(original_word_letters) 
trails = len(original_word_letters) * 3
current_index = 0
failed = 0
user_list = []
def game(current_index,trails,failed,user_list):
    print(f"Your trails is : {trails}")
    user_input = input(f"Enter the letter num {current_index+1} : ") # entered y
    trails-=1
    if trails > 0:
        if user_input == original_word_letters[current_index]:
            failed = 0
            current_index+=1
            print(f"Great, you cach it the letter was : {user_input}")
            user_list.append(user_input)
            if original_word_letters == user_list:
                print(f"Congratulations, You got it the word was : {"".join(original_word_letters)}")
                quit()
            else:
                game(current_index,trails,failed,user_list)
        else:
            failed+=1
            if failed < 3:
                print("Oops, it's wrong TRYAGAIN")
                game(current_index,trails,failed,user_list)
            else:
                random.shuffle(original_word_letters)
                print("We have Re-Ordered the word again, Catch it")
                failed = 0
                current_index = 0
                game(current_index,trails,failed,user_list)
    else:
        print("You Finished your trails, TRYAGAIN LATER")
        quit()


game(current_index,trails,failed,user_list)
    