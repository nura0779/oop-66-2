class Hero:
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет я {self.name}, мой уровень {self.lvl}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.hp += 1

hero1 = Hero("kirito", 100, 1000, 200)
hero2 = Hero("asuna", 100, 1100, 300)

hero1.greet()
hero1.attack()
hero1.rest()
print(hero1.hp, hero1.strength)


hero2.greet()
hero2.attack()
hero2.rest()
print(hero2.hp, hero2.strength)