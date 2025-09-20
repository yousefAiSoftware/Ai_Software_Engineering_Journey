class Employee:
    raise_amount = 1.04
    def __init__(self, fName, lName, phone, salary):
        self.fName = fName
        self.lName = lName
        self.phone = phone
        self.salary = salary
    @property
    def fullname(self):
        return "{} {}".format(self.fName , self.lName)
    def apply_raise(self):
        self.salary = int( self.salary * self.raise_amount )
    def __repr__(self):
        return "Employee Class Object : {} , {} , {}".format(self.fullname,self.phone,self.salary)
    def __str__(self):
        return "{} - {}".format(self.fullname,self.phone)
    def __add__(self,other):
        return self.salary + other.salary
    def __len__(self):
        return len(self.fullname)
    @property
    def email(self):
        return "{}{}@company.com".format(self.fName,self.lName)
    @fullname.setter
    def fullname(self, name):
        self.fName , self.lName = name.split(" ")

    

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, fName, lName, phone, salary, programming_language):
        super().__init__(fName, lName, phone, salary)
        self.programming_language = programming_language
    def __repr__(self):
        return "Devoloper Class Object : {} , {} , {}".format(self.fullname,self.phone,self.salary)

class Manager(Employee):
    def __init__(self, fName, lName, phone, salary, employees=None):
        super().__init__(fName, lName, phone, salary) 
        # Employee.__init__(self, fName, lName, phone, salary) --> THe same functionality of the above line 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def display_emps(self):
        for emp in self.employees:
            print("-->" , emp.fullname)
    def __repr__(self):
        return "Manager Class Object : {} , {} , {}".format(self.fullname,self.phone,self.salary)
        



emp1 = Developer("Anas","Anwar","66514263",5000, "Python")
emp2 = Developer("Tarik","Saeed","55110258",5000, "Python")

mgr1= Manager("Yousef","Ahmed","91101180",12000,[emp1])





emp2.fullname = "Omar Alsulaily"


print(emp1 + mgr1)
print(len(emp2))
print(mgr1.email)
print(emp2.fullname)