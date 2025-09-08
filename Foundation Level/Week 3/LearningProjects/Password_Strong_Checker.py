print("Welcome to our Strong Password Checker...")
password = input("Enter the password :")
special = ["@","#","$","%","&","(",")","*"]
isnum = False
iscapital = False
isspecial = False
islength = False
if len(password) >= 8:
    islength = True
for i in password:
    if i.isupper() == True:
        iscapital = True
        continue;
    if i.isdigit() == True:
        isnum = True
        continue;
    if i in special:
        isspecial = True
        continue;
    

if isnum and iscapital and isspecial and islength:
    print("Your Password is Accepted !")
else:
    print("Your Password is Rejected ~")


