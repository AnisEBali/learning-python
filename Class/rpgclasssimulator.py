class Character:
    # Class attribute shared by all characters:
    faction = "Guild of Legends"

    def __init__(self,name,level):
       # Instance attribute: 
        self.name = name
        self.level = level
        self.health = 100 + level * 10 #(To scale with level)

    def intro(self):
        print(f"{self.name}, Level: {self.level}, of the {self.faction}")

class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a mighty sword!")

class Mage(Character):
    def castSpell(self):
        print(f"{self.name} casts *fireball*!")

class Rogue(Character):
    def steal(self):
        print(f"{self.name} sneaks behind and steals some gold!")

hero1 = Warrior("Arthas", 5)
hero2 = Mage("Merlin", 8)
hero3 = Rogue("Valeera", 6)

hero1.intro()
hero1.attack()

hero2.intro()
hero2.castSpell()

hero3.intro()
hero3.steal()

