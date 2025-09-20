class Student:
    students_num = 0
    uv = "KCST"
    def __init__(self, name, id, GPA, major, passed_credits):
        self.name = name
        self.id = id
        self.GPA = GPA
        self.full_credits = 144
        self.major = major
        self.passed_credits = passed_credits
        self.remaining_credits = self.full_credits - self.passed_credits
        Student.students_num += 1
    def display(self):
        print(f"{self.name} is a student in {Student.uv} Collage , has an id : '{self.id}' , major : {self.major} , GPA : {self.GPA} , his remaning credits is : {self.remaining_credits}")
    
print(Student.students_num)
std1 = Student("Yousef", "231419", 3.88, "CE" , 74)
print(std1.students_num)
std1.display()
std2 = Student("Omar", "226412" , 2.48, "CE" , 61)
print(std2.students_num)
std2.display()

print("\n------------------------------\t---------------------------------\n")



class Customer:
    customers_num = 0
    discount = 0.05
    def __init__(self, name, balance,):
        self.name = name
        self.balance = balance
        if self.balance > 50000:
            self.discount = 0.15
        Customer.customers_num += 1
    def calc_price(self,price):
        final_price = price * (1 - self.discount)
        return final_price
    

customer1 = Customer("Yousef", 70000)
customer2 = Customer("Ali", 25000)
print(customer1.calc_price(510))
print(customer2.calc_price(510))

