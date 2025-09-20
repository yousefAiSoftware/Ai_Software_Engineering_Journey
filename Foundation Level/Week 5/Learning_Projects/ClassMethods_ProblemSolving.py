class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    @classmethod
    def from_string(cls,str):
        brand,model,year = str.split("-")
        return cls(brand,model,int(year))
    def display(self):
        print(f"This is: {self.brand} {self.model} {self.year}")
    
car1 = Car("Nissan","Altima",2008)
car2 = Car.from_string("Honda-Odessy-2015")

car1.display()
car2.display()


print("\n----------------------------\t----------------------------\n")

class Converter:
    @staticmethod
    def cm_to_inches(cm):
        inches = cm / 2.54
        return inches
print(Converter.cm_to_inches(10))






print("\n----------------------------\t----------------------------\n")


