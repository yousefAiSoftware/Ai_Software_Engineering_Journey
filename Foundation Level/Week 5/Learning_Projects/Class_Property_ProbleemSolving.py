def Divider():
    print("\n--------------------------------\t--------------------------------\n")
class Tempreture:
    def __init__(self, temp):
        self.temp = temp
    @property
    def celsius(self):
        return "The tempreture is : {} Celsius".format(self.temp)
    @celsius.setter
    def celsius(self, temp):
        if temp >= -273.15:
            self.temp = temp
        else:
            raise ValueError
    @property
    def fahrenheite(self):
        new_temp = self.temp * (9/5) + 32
        return "The Tempreture is : {} Fahrenheite".format(new_temp)
    @fahrenheite.setter
    def fahrenheite(self, temp):
        new_temp = (temp - 32) * (5/9)
        self.celsius = new_temp


temp1 = Tempreture(59)
print(temp1.celsius)
temp1.fahrenheite = 85
print(temp1.fahrenheite)
print(temp1.celsius)

Divider()

class WebsiteUser:
    def __init__(self, username):
        self._username = username
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if (username.strip()).isalnum() and len(username.strip()) >= 4:
            self._username = username
        else:
            raise ValueError

class Moderator(WebsiteUser):
    def __init__(self, username):
        super().__init__(username)
    @property
    def username(self):
        return self._username + " --> (Moderator)"
    @username.setter
    def username(self, username):
        if (username.strip()).isalnum() and len(username.strip()) >= 4 and (username.strip()).lower() != "admin":
            self._username = username.strip()
        else:
            raise ValueError

moderator1 = Moderator("Yousef")
moderator1.username = "Yousfe123 "


print(moderator1.username)


Divider()


class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        if width > 0 :
            self._width = width
        else:
            raise ValueError
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError
    @property
    def area(self):
        return self.width * self.height
    def __str__(self):
        return "Rectangle : Width : {} , Height : {} , Area : {}".format(self.width,self.height,self.area)
    def __eq__(self, other):
        if self.area == other.area:
            return True
        else:
            return False
    @classmethod
    def create_square(cls, rip_value):
        if rip_value > 0 :
            return cls(rip_value,rip_value)
        else:
            raise ValueError
            

square1 = Rectangle.create_square(7)
rect1 = Rectangle(5,5)
rect2 = Rectangle(10,2.5)
print(square1.area)
print(square1 == rect1)
print(square1 == rect2)
rect1.height = 1.5
print(rect1)

Divider()

class PremiumAccount:
    def __init__(self, owner, balance, overdraft_limit = 1000):
        self._owner = owner
        self._balance = balance
        self._overdraft_limit = overdraft_limit
    def withdraw(self, value):
        if value <= self._balance + self._overdraft_limit:
            new_balance = self._balance - value
            print(f"Succesful !, Withdrawn '{value}' from your account balance '{self._balance}', your new account balance is : {new_balance}")
            self._balance = new_balance
        else:
            raise ValueError
    def deposit(self, value):
        new_balance = self._balance + value
        print(f"Succesful !, Deposited '{value}' to your account balance '{self._balance}', your new account balance is : {new_balance}")
        self._balance = new_balance
    @property
    def overdraft_limit(self):
        return self._overdraft_limit
    @overdraft_limit.setter
    def overdraft_limit(self, value):
        if value > 0 :
            self._overdraft_limit = value
        else:
            raise ValueError
    @overdraft_limit.deleter
    def overdraft_limit(self):
        if self._balance < 0 :
            print("Can't Delete overdraft limit, You are using it")
            raise Exception
        else:
            self._overdraft_limit = 0


my_account1 = PremiumAccount("Yousef", 50000)
del my_account1.overdraft_limit
my_account2 = PremiumAccount("Yousef", 50000, 30000)
my_account2.withdraw(10000)
del my_account2.overdraft_limit

        
Divider()


class InventoryItem:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, val):
        if val > 0:
            self._quantity = val
        else:
            raise ValueError
    @property
    def total(self):
        return 0
class SellableItem(InventoryItem):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, val):
        if val > 0:
            self._price = val
        else:
            raise ValueError
    @property
    def total(self):
        return self._price * self._quantity
class Inventory:
    def __init__(self):
        self._items = {}
    def add_item(self, item):
        if isinstance(item,InventoryItem) or isinstance(item,SellableItem):
            self._items.update({item._name : item})
    def __len__(self):
        return len(self._items)
    @property
    def inventory_total(self):
        total =0
        if len(self) > 0 :
            for item in self._items.values():
                total += item.total
            return total
        else:
            raise ValueError

main_inventory = Inventory()
item1 = SellableItem("iPhone", 4 , 1199)
item2 = SellableItem("Laptop", 8, 1599)
item3 = InventoryItem("Book", 25)
main_inventory.add_item(item1)
main_inventory.add_item(item2)
main_inventory.add_item(item3)
len(main_inventory)
print(main_inventory.inventory_total)


        
    
    