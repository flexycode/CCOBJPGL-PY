class Character:
    def __init__(self, health, attack, defense, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.name = name

    def sayMyName(self):
        print("My name is", self.name)


knight = Character(10, 5, 0, "Chen")
knight.sayMyName()

mage = Character(0, 5, 10, "Akasha")
mage.sayMyName()

thief = Character(5, 10, 0, "Gondar")
thief.sayMyName()