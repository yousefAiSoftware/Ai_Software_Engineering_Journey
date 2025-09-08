print("Welcome to our target Pairs App...")
num_list = []
target = int(input("Enter the target num : "))
while True:
    user_input = int(input("Enter the num (-1 to exit) : "))
    if user_input == -1:
        break;
    num_list.append(user_input)
current_index = 0
for i ,num in enumerate(num_list):
    if num > target:
        continue;
    if num == target:
        print(f"Founded the same num in the list : {num_list[current_index]}")
        continue;
    current_index = i+ 1
    while current_index < len(num_list):
        if num_list[current_index] == (target - num):
            pair = num_list[current_index]
            print(f"Founded pairs sum of '{target}' is : {num} + {pair} ")
        current_index+=1
else:
    print(f"Cannot Found pairs sum of : {target}")



        
    
