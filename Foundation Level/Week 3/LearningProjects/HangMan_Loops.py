print("Welcome To our HangMan Game : ")
password = "AmoAboKhozayem"
password_letters = list(password)
user_list = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_",]
lives = 5
failed = 0
trails = len(password_letters) + 5
def game(password_letters,failed,lives,user_list,trails):
    while trails > 0 :
        user_input = input("Enter the letter : ")
        trails-=1
        if user_input in password_letters:
            if user_input not in user_list:
                print(f"Correct, The word has : {user_input}")
                check(user_input,password_letters,user_list)
                if user_list == password_letters:
                    print(user_list)
                    print(f"Congratulations, You Got it the passwors was : {password}")
                    break;
                else:
                    failed = 0
                    print(user_list)
                    print(f"Your Score is => Trails : {trails} , Lives : {lives} , Failed : {failed}")
            else:
                print(f"the letter '{user_input}' is already added.")
        else:
            failed+=1
            print("TRYAGAIN~~~")
            if failed == 2:
                lives-=1
                print("You entered two incorrect following so, your lives decreased")
                print(f"Your Score is => Trails : {trails} , Lives : {lives} , Failed : {failed}")
                failed = 0
                if lives == 0:
                    print("Your lives reached to '0', You Lose~~~")
                    break;
            else:
                print(f"Your Score is => Trails : {trails} , Lives : {lives} , Failed : {failed}")
    else:
        print("Your trails reached to '0', You Lose~~~")
        

def check(user_input,password_letters,user_list):
    for i , letter in enumerate(password_letters):
        if user_input == letter:
            user_list[i] = user_input




game(password_letters,failed,lives,user_list,trails)