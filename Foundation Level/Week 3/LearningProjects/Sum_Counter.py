import random
print("Welcome To our counter app")
sum_counter = 0
current_index = 0
while sum_counter <= 50: 
    computer_num = random.randint(0,10)
    sum_counter+=computer_num
    print(f"The sum is : {sum_counter}")
    current_index+=1
else:
    print(f"It takes {current_index} to reah 50 ")