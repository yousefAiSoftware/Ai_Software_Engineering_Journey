class Cart:
    tax = 0.07
    def __init__(self, istax=True):
        self.items = {}
        self.istax = istax
    def add_item(self,name,quantity,price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items.update({name : {"quantity" : quantity , "price" : price}})
    def calc_total(self):
        price_sum = 0
        item_price = 0
        for value in self.items.values():
            item_price = value["quantity"] * value["price"]
            price_sum += item_price
        if self.istax:
            total = price_sum + (price_sum * Cart.tax)
        else:
            total = price_sum
        return total
    

cart1 = Cart()
cart1.add_item("Book",3,12.5)
cart1.add_item("Mic",1,150)
cart1.add_item("Book",4,12.5)
cart2 = Cart(False)
cart2.add_item("shoes", 2, 25)
cart2.add_item("Headphone", 1, 30)
print(cart1.calc_total())
print(cart2.calc_total())


        