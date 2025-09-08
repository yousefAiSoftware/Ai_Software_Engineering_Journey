print("Welcome to our Collatz Conjecture App...")
user_num = int(input("Enter the Positive num : "))
if user_num < 0 :
    print("Invalid Value !")
else:
    while user_num != 1:
        if user_num % 2 == 0:
            user_num /= 2
            print(int(user_num))
        else:
            user_num  = (user_num * 3) + 1 
            print(int(user_num))