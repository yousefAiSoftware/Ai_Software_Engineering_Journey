class MediaItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"This MediaItem has Title : {self.title} , Author : {self.author}")

class Book(MediaItem):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def display_info(self):
        # super().display_info() --> can call the super class method
        print(f"This Book has : {self.title} , Author : {self.author}, Pages : {self.page_count}")

book1 = Book("saheh albokhary","Albokhary",4562)
book1.display_info()

def Divider():
    print("\n-----------------------------------------\t-----------------------------------------\n")

Divider()

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Default Animal Sound")
    
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("Lion Sound")

class Penguin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("Penguin Sound")
    def swim(self):
        print(f"{self.name} can swim")


lion1 = Lion("Zack", 4)
penguin1 = Penguin("Twir",95) 
zoo_animals = [lion1,penguin1]
for animal in zoo_animals:
    print(animal.name)
    animal.make_sound()
    if isinstance(animal,Penguin):
        animal.swim()


Divider()


class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = float(balance)
    def withdraw(self, amount):
        if self.balance > amount:
            new_account_balance = self.balance - amount
            print(f"{amount} withdrawed succesfully from your account balance : {self.balance}, your new account balance is : {new_account_balance}")
            self.balance = new_account_balance
        else:
            print("Not enough Balance to withdraw")

class CheckingAccount(BankAccount):
    transaction_fee = 1.5
    def withdraw(self, amount):
        if self.balance > (amount + CheckingAccount.transaction_fee):
            super().withdraw(amount + CheckingAccount.transaction_fee)
        else:
            print("Not enough Balance to withdraw")

account1 = CheckingAccount("Yousef Account", 3500)
account1.withdraw(3000)




Divider()

import random
class Vehicle:
    max_speed = 120
    def __init__(self, lisence_plate):
        self.lisence_plate = lisence_plate
    @classmethod
    def create_with_random_plate(cls):
        cls.random_license_plate = random.randint(11111,99999)
        return cls(cls.random_license_plate)

class Truck(Vehicle):
    max_speed = 80
    def __init__(self, lisence_plate, capacity):
        super().__init__(lisence_plate)
        self.capacity = capacity
    @classmethod
    def create_with_random_plate(cls, capacity= 1000):
        random_license_plate = random.randint(11111,99999)
        return cls(random_license_plate,capacity)

v1 = Vehicle.create_with_random_plate()
t1 = Truck.create_with_random_plate(1500)
print(v1.max_speed)
print(t1.max_speed)
print(t1.capacity)


Divider()

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
    @classmethod
    def create_new_order(cls):
        random_id = random.randint(100,999)
        return cls(random_id)
    def display(self):
        print(f"This Order Created : {self.order_id}",end=" ")

class DeliveryOrder(Order):
    def __init__(self, order_id, delivery_adress):
        super().__init__(order_id)
        self.delivery_adress = delivery_adress
    @classmethod
    def create_new_order(cls, adress):
        random_id = random.randint(100,999)
        return cls(random_id,adress)
    def display(self):
        return super().display() , print(f"{self.delivery_adress}")
    
order1 = Order.create_new_order()
order1.display()
print("\n")
order2 = DeliveryOrder.create_new_order(", Adress : 123 home 123")
order2.display()


Divider()


class File:
    def __init__(self, filename, size):
        self.filename = filename
        self.size = size
    @classmethod
    def create_untitled(cls, size):
        filename = "UnTitled"
        return cls(filename,size)
    def info(self):
        return f"{self.filename} Created with size : {self.size}"

class ImageFile(File):
    def __init__(self, filename, size, resolution):
        super().__init__(filename, size)
        self.resolution = resolution
    @classmethod
    def create_untitled(cls,resolution):
        filename = "untitled.png"
        size = 500
        return cls(filename, size, resolution)
    def info(self):
        return super().info() + f", resolution : {self.resolution}"

file1 = File.create_untitled(100)
file2 = ImageFile.create_untitled("1920*1080")

print(file1.info())
print(file2.info())
    

Divider()

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    @classmethod
    def new_player(cls, name):
        level = 1
        return cls(name, level)
    def info(self):
        info = f"{self.name} Created with level : {self.level}"
        return info

class ElitePlayer(Player):
    def __init__(self, name, level, special_item):
        super().__init__(name, level)
        self.special_item = special_item
    @classmethod
    def new_player(cls, name, special_item = "Sword"):
        level = 10
        return cls(name, level, special_item)
    def info(self):
        return super().info() + f", special item : {self.special_item}"
    
player1 = Player.new_player("Anas")
player2 = ElitePlayer.new_player("Yousef", "Gun")

print(player1.info())
print(player2.info())


Divider()

class SuperHero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
class FlightEnabled:
    def fly(self):
        print("Flying Enabled !")
class TechPower:
    def tech(self):
        print("Tech Power Enabled !")

class SuperMan(SuperHero,FlightEnabled):
    def __init__(self, name, power):
        super().__init__(name, power)

class BatMan(SuperHero,TechPower):
    def __init__(self, name, power):
        super().__init__(name, power)

my_hero1 = SuperMan("Zack","Flying")
print(my_hero1.name)
my_hero1.fly()
my_hero2 = BatMan("Shawlin","Tech")
print(my_hero2.power)
my_hero2.tech()


    