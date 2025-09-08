print("Welcome to our day detector app")
days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
user_day = input("Enter the day : ")
user_num = int(input("Enter the number of days : "))

def calc_day():
    if user_day in days:
        user_day_num = days.index(user_day)
        next_day = (user_day_num + user_num) % 7
        print(f"The day after '{user_num}' days of '{user_day}' is : '{days[next_day]}'")
    else:
        print("Invalid Value")
        quit()
        

calc_day()
