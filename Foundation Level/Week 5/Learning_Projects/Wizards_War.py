class Wizrad:
    max_health = 100
    max_mana = 50
    def __init__(self, name):
        self.name = name
        self.health = Wizrad.max_health
        self.mana = Wizrad.max_mana
    def attack(self, wizard):
        if self.mana >= 10:
            self.mana -= 10
            wizard.take_damage()
    def take_damage(self):
        self.health -= 20
        print(f"{self.name} has remaning health : {self.health}")
    def displsy(self):
        print(f"'{self.name}' has Health : {self.health} , Mana : {self.mana}")
    

wiz1 = Wizrad("Harry Poter")
wiz2 = Wizrad("Foldmort")

wiz1.attack(wiz2)
wiz1.attack(wiz2)

wiz1.displsy()
wiz2.displsy()

