class Employee:
    def __init__(self, fName, lName, phone, salary):
        self.fName = fName
        self.lName = lName
        self.phone = phone
        self.salary = salary
    def fullname(self):
        return "{} {}".format(self.fName , self.lName)
    

emp1 = Employee("Yousef","Ahmed","91101180",5000)
print(emp1.fullname())
