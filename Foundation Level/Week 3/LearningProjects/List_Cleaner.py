print("Welcome to our list Cleaner App..")
user_list = []
cleaned_list = []
while True:
    user_item = input("Enter the item : ").lower()
    if user_item == "done":
        print()
        break;
    user_list.append(user_item)
for item in user_list:
    if item not in cleaned_list:
        cleaned_list.append(item)
print(f"Your Original list is : {user_list}")
print(f"Your Cleaned list is : {cleaned_list}")
