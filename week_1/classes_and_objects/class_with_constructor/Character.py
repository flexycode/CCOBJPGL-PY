class Character:
    def __init__(self, strength, agility, intelligence, name):
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.name = name

    def sayMyName(self):
        print("Hello, I am", self.name)


knight = Character(10, 5, 0, "Chen")
knight.sayMyName()

mage = Character(0, 5, 10, "Akasha")
mage.sayMyName()

thief = Character(5, 10, 0, "Gondar")
thief.sayMyName()