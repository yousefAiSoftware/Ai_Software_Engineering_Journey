# ده حلي 
print("Greeting!....Welcome to our week day detect app !...")
day = input("Enter the Week Day you want ? : ")
x_days = int(input("Enter the number days After ?  (should be : positive integers) :  "))
week = { "sunday" : 0   ,  "monday" : 1 ,   "tuesday" : 2 ,   "wednesday" : 3 , "thursday" : 4 , "friday" : 5 , "saturday" : 6 }
week_key = { 0 : "sunday" ,  1 : "monday" ,  2  : "tuesday",  3 : "wednesday" , 4 : "thursday" ,  5 : "friday" ,  6 : "saturday" }

def calc_day():
    day_num = week[day]
    new = (day_num + x_days) % 7
    ans = f"the day after {x_days} days is : {week_key[new]}"

    return ans

print(calc_day())

# ده حل تشات جبت اللي هو more logical وابسط 
print("Greeting!....Welcome to our week day detect app !...")
day = input("Enter the Week Day you want? : ").lower()
x_days = int(input("Enter the number of days after? : "))

week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def calc_day():
    day_num = week.index(day)  # بدل استخدام قاموس
    new_day = week[(day_num + x_days) % 7]  # نفس logic mod 7
    return f"The day after {x_days} days is: {new_day}"

print(calc_day())
