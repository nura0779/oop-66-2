import random

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

class Warrior(Hero):
    def __init__(self, name, lvl, hp, strength, stamina):
        super().__init__(name, lvl, hp, strength)
        self.stamina = stamina
    def attack(self):
        print("Воин атакует мечом!")

class Mage(Hero):
    def __init__(self, name, lvl, hp, strength, mana):
        super().__init__(name, lvl, hp, strength)
        self.mana = mana
    def attack(self):
        print("Маг кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, lvl, hp, strength, stealth):
        super().__init__(name, lvl, hp, strength)
        self.stealth = stealth
    def attack(self):
        print("Ассасин атакует из-под тишка!")

Warrior("Warrior", 100, 1000, 50, 100)
Mage("Mage", 98, 100, 60, 500)
Assassin("Assassin", 101, 100,70,98)

heroes = {
    "Warrior": Warrior,
    "Mage": Mage,
    "Assassin": Assassin
}

choice = input("Выбери героя: Warrior/Mage/Assassin: ")

player = heroes[choice]
enemy_name = random.choice(list(heroes.keys()))
enemy = heroes[enemy_name]

print("Вы выбрали:", choice)
print("Противник:", enemy_name)
if choice == enemy_name:
    print("Ничья")

elif (choice == "Warrior" and enemy_name == "Assassin") or \
     (choice == "Assassin" and enemy_name == "Mage") or \
     (choice == "Mage" and enemy_name == "Warrior"):
    print(choice, "победил!")
else:
    print(enemy_name, "победил!")