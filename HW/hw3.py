from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, lvl, strength, health):
        self.name = name
        self.lvl = lvl
        self.strength = strength
        self.__health = health

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def rest(self):
        print(f"{self.name} отдыхает..")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass
class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")

class Mage(Hero):
    def attack(self):
        print("Маг использует магию")

class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка")

warrior = Warrior("asuna", 50, 100, 200)
mage = Mage("kirito", 60, 70,200,)
assassin = Assassin("Merlin", 90, 58, 160)

warrior.greet()
warrior.attack()
warrior.rest()
print()
mage.greet()
mage.attack()
mage.rest()
print()
assassin.greet()
assassin.attack()
assassin.rest()

