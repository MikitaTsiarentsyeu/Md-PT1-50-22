
class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return self.name

class Animal:

    def __init__(self, name) -> None:
        self.name = name

    def eat(self, something):
        print(f"eating {something}")

    def phe(self):
        print("phe...")

    def __str__(self) -> str:
        return self.name

class Carnivore(Food, Animal):

    def __init__(self, name, breed) -> None:
        Animal.__init__(self, name)
        Food.__init__(self, name, "meat")
        self.breed = breed

    def eat(self, something):
        if something.type == "meat":
            Animal.eat(self, something)
        else:
            Animal.phe(self)

class Herbovore(Food, Animal):

    def __init__(self, name, breed) -> None:
        Animal.__init__(self, name)
        Food.__init__(self, name, "meat")
        self.breed = breed

    def eat(self, something):
        if something.type == "grass":
             Animal.eat(self, something)
        else:
            Animal.phe(self)

class Omnivore(Carnivore, Herbovore):

    def __init__(self, name, breed) -> None:
        super().__init__(name, breed)

    def eat(self, something):
        if something.type == "meat":
            Carnivore.eat(self, something)
        elif something.type == "grass":
            Herbovore.eat(self, something)
        else:
            Animal.phe(self)


steak = Food("steak", "meat")
grass = Food("grass", "grass")
poo = Food("poo", "poo")

c = Carnivore("Zephirka", "wss")
h = Herbovore("Moo-Moo cow", "black and white cow")
o = Omnivore("Petya", "human")

food = [steak, grass, poo]
animals = [c, h, o]

for f in food:
    for a in animals:
        print(f"{a} is trying to eat {f}:")
        a.eat(f)
    