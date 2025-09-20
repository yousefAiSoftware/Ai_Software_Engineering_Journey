import os
users_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"users.txt")
class DataValidator:
    
    @classmethod
    def fromfile(cls,txtfile):
        words = []
        with open(txtfile , "r") as file:
            for line in file:
                words.append((line.strip().split(",")))
        return words
    
    @staticmethod
    def is_valid_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False
    
    @staticmethod
    def is_valid_password(password):
        valid = False
        if len(password) >= 8 :
            for letter in password:
                if not letter.isdigit():
                    valid
                    continue;
                valid = True
            return valid
        else:
            return valid
    @staticmethod
    def check(users_list):
        for user in users_list:
            if DataValidator.is_valid_email(user[0]) and DataValidator.is_valid_password(user[1]):
                print(f"{user} is Valid")
            else:
                print(f"{user} is InValid")



users_list = DataValidator.fromfile(users_file)

DataValidator.check(users_list)