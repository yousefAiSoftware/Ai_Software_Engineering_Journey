#ده حلي صح واللوجيك مظبوط بس عدد المحاولات كان مرات يتلخبط بسبب عدم ترتيب وقت تصفير العداد وزيادة عدد المحاولات
import random
print("WELCOME TO OUR GUESS GAME!!!")
num = [1,2,3,4,5]
computer_choice = random.choice(num)
player_inputs = 1;
player_correct = 0;


def again():
    ask = input("Do you want to play again? (y/n) : ")
    if ask == "y" :
        game()
        
    else :
        quit

def game():
    global computer_choice;
    global player_inputs;
    global player_correct;
    player_guess = int(input("Enter your Guessed NUM ? (1 , 2 , 3 , 4 , 5) :"))
    if player_guess not in num  :
        print("Out OF Range Value ! ")
        player_inputs = player_inputs + 1;
        game()
    else:
        if player_inputs <= 3 :
            if player_correct == 2 :
                player_inputs = player_inputs + 1;
                player_correct = player_correct + 1;
                print("You Won The Game!!!\n THANKYOU FOR PLAYING...")
                player_inputs = 1;
                player_correct = 0;
                again()
            else:
                player_inputs = player_inputs + 1;
                if player_guess == computer_choice :
                    player_correct = player_correct + 1;
                    print(f"You guessed correct num it was {player_guess}")
                    computer_choice = random.choice(num)
                    game()
                else :
                    print("It's not correct, you need to try again... ")
                    game()
        else :
            print("you finished your trials,,, TRY AGAIN LATER...")
            player_inputs = 1;
            player_correct = 0;
            again()    
game()
           
















#ده حل تشات جبت بعد ما انا وقف معي الموضوع في خطوة عدد المحاولات

import random

print("WELCOME TO OUR GUESS GAME!!!")

num = [1, 2, 3, 4, 5]

# اختيار الرقم العشوائي الأولي
computer_choice = random.choice(num)

# العدادات العالمية
player_inputs = 0    # تبدأ من 0 لأنه أول محاولة لم تتم بعد
player_correct = 0


def again():
    # إعادة اللعبة إذا أراد اللاعب
    ask = input("Do you want to play again? (y/n) : ")
    if ask.lower() == "y":
        # إعادة تعيين العدادات والرقم قبل بدء اللعبة الجديدة
        global player_inputs, player_correct, computer_choice
        player_inputs = 0
        player_correct = 0
        computer_choice = random.choice(num)
        game()
    else:
        print("Thanks for playing!")
        quit()


def game():
    global computer_choice
    global player_inputs
    global player_correct

    # أخذ التخمين من اللاعب
    player_guess = int(input("Enter your Guessed NUM ? (1 , 2 , 3 , 4 , 5) : "))

    # **زيادة المحاولة لكل إدخال مهما كان**
    player_inputs += 1

    # التحقق من أن الرقم ضمن النطاق
    if player_guess not in num:
        print("Out OF Range Value!")
        # تحديث الرقم العشوائي هنا ليس مطلوب حسب المطلوب، يبقى كما هو
    else:
        # التحقق من صحة التخمين
        if player_guess == computer_choice:
            player_correct += 1
            print(f"You guessed correct num it was {player_guess}")
            computer_choice = random.choice(num)
            # **تحديث الرقم فقط إذا كان التخمين خاطئ حسب المطلوب**
        else:
            print("It's not correct, you need to try again...")
              # تحديث الرقم بعد خطأ

    # التحقق من الفوز: 2 إجابة صحيحة
    if player_correct >= 2:
        print("You Won The Game!!!\nTHANK YOU FOR PLAYING...")
        again()
        return  # مهم جداً: نوقف أي استدعاءات قديمة متبقية في recursion

    # التحقق من انتهاء المحاولات: 3 محاولات
    if player_inputs >= 3:
        print("You finished your trials,,, TRY AGAIN LATER...")
        again()
        return  # مهم: نوقف أي استدعاءات متبقية

    # إذا لم ينتهِ شيء، نعيد اللعبة للمحاولة التالية
    game()

game()

















 


