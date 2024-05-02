class Character:
    def sayMyName(self):
        print("Hello, I am", self.name)


knight = Character()
knight.strength = 10
knight.agility = 5
knight.intelligence = 0
knight.name = "Chen"
knight.sayMyName()

mage = Character()
mage.strength = 0
mage.agility = 5
mage.intelligence = 10
mage.name = "Akasha"
mage.sayMyName()

thief = Character()
thief.strength = 5
thief.agility = 10
thief.intelligence = 0
thief.name = "Gondar"
thief.sayMyName()