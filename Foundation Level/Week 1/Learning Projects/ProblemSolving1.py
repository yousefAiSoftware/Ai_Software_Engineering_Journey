print("Welcome to Area Game")

def area():
    w = int(input("Enter the rect width : "))
    l = int(input("Enter the rect length : "))
    return l * w
max_area = 0
def again():
    global max_area
    rect_area = area()
    print(f"the area of this rect is : {rect_area} \n------------------------")
    if max_area < rect_area :
        max_area = rect_area
    ans = input("Do you want to add rect ? (y/n) :")
    if ans == "y":
        again()
    elif ans == "n":
        print(f"the biggest area is : {max_area}")
    else:
        print("Invalid Value! , Enter (y/n) :")
        again()

again()