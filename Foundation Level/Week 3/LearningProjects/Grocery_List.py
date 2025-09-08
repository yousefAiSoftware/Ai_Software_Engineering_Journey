print("Welcome to our Grocery List App...")
def My_grocery():
    user_list = []
    while True:
        user_item = input("Enter the item : ").lower()
        if user_item == "done":
            break;
        else:
            if user_item in user_list:
                print("Already Added !")
                continue;
            else:
                user_list.append(user_item)
                print("OK added, what's next ?")
    print(f"Your list is : {user_list}")
My_grocery()

def Perfectgrocery():
    user_list = []
    while True:
        user_item = input("Enter the item : ").lower()

        # الحالة الأولى: الخروج من اللوب
        if user_item == "done":
            break

        # الحالة الثانية: العنصر مكرر
        if user_item in user_list:
            print("Already Added !")
            continue

        # إذا لم يتحقق أي مما سبق، فالمدخل جديد وصالح
        user_list.append(user_item)
        print("OK added, what's next ?")

    print(f"Your list is : {user_list}")

Perfectgrocery()