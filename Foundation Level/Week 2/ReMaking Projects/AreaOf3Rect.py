print("Welcome to our rect area Calc")

max_area = 0
min_area = 9999999999

def Area():
    w = int(input("Enter the rect width : "))
    l = int(input("Enter the rect length : "))
    area = w*l
    print(f"The Rect area is : {area}\n--------------------------")
    calc_Maximum(area)
    calc_Minimum(area)
    again()
    return area
def calc_Maximum(area):
    global max_area
    if max_area < area:
        max_area = area
    return max_area
    
def calc_Minimum(area):
    global min_area
    if min_area > area:
        min_area = area
    return min_area

def again():
    ask = input("Do you want add another rect (y/n) ? : \n-----------------------------")
    if ask == "y":
        Area()
    elif ask == "n":
        print(f"--------------------------\nThe biggest rect has Value : {max_area},\t the smallest has value : {min_area}")
        quit()
    else:
        print("Invalid Value, Try Again")
        again()





Area()
