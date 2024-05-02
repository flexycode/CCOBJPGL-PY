class Character:
    def __init__(self, strength, agility, intelligence, name):
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.name = name

    def sayMyName(self):
        print("Hello, I am", self.name)

    def sayMyStrength(self):
        print("My strength is", self.strength)


character = Character(10, 5, 0, "Chen")
character.sayMyName()
character.sayMyStrength()
