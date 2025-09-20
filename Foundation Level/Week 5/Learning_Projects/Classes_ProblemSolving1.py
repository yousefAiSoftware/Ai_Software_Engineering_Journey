class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    
    def display_info(self):
        print(f"This is {self.brand} {self.model} built in {self.year}.")
    
car1 = Car("Ford","F150","2022")
car1.display_info()
car2 = Car("Marcedis","Mybakh","2024")
Car.display_info(car2) # This is what python do behind the scene when we use <<<<<<  car2.display_info()  >>>>>

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.isopen = False
    
    def summary(self):
        print(f"this book {self.title} by {self.author} has {self.pages} pages")
    
    def openbook(self):
        self.isopen = True
        print("This book now is opened")
    
    def closebook(self):
        self.isopen = False
        print("This book now is closed")

book1 = Book("Poor dad rich dad", "Robert Kusaky", 870)
book1.summary()
book1.openbook()
book2 = Book("Atomic Habits", "James Clear", 320)
book2.summary()
book2.closebook()


class Circle:
    def __init__(self, raduis):
        self.raduis = raduis

    def calc_area(self):
        return 3.1415 * (self.raduis ** 2)
    
    def calc_circumference(self):
        return 3.1415 * 2 * self.raduis
    
circle1 = Circle(5)
print(circle1.calc_area())
circle2 = Circle(7.5)
print(circle2.calc_circumference())
    

