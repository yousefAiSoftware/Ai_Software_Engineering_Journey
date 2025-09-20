class Item:
    pay_rate = 0.8
    all_items = []
    def __init__(self, name:str, price:float, quantity:int):
        assert len(name) >= 3 , f"{name} has no name meaning"
        assert price >= 0 , "Price should be greater than or equal 0"
        assert quantity >= 0 , "Quantity should be greater than or equal 0"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)
    def calc_total(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price *= self.pay_rate
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
item1 = Item("Car",5500,2)
item2 = Item("iPhone", 1199, 8)
print(item1.calc_total())
print(item2.calc_total())
print(Item.all_items)