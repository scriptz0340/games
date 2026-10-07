import random
import breeds

id_file = open("id_file.txt", "r")
used_ids = id_file.readlines()
id_file.close()
    

class Character:

    def __init__(self, name, breed):
        self.name = name
        self.rank = "Newborn"
        self.breed = breed
        self.vc = 200
        self.id = random.randint(0, 1000)
        self.health = 100
        self.prompt = breeds.aura.prompt
        if self.id in used_ids:
            self.id = random.randint(0, 1000)
        used_ids.append(self.id)
        if self.breed == 'Dev':
            self.rank = "Master"
            self.vc = 1000000
        

    def show_info(self):

        print("-------------------------")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print(f"\x1b[48;5;223m     \x1b[96mName: \x1b[97m{self.name}\x1b[0m\x1b[0m \x1b[0m")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print(f"\x1b[48;5;223m     \x1b[96mRank: \x1b[97m{self.rank}\x1b[0m\x1b[0m \x1b[0m")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print(f"\x1b[48;5;223m     \x1b[96mBreed: \x1b[97m{self.breed}\x1b[0m\x1b[0m \x1b[0m")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print(f"\x1b[48;5;223m     \x1b[96mVc: \x1b[97m{self.vc}\x1b[0m\x1b[0m   \x1b[0m")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print(f"\x1b[48;5;223m     \x1b[96mId: \x1b[97m{self.id}\x1b[0m\x1b[0m   \x1b[0m")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print(f"\x1b[48;5;223m     \x1b[96mHealth: \x1b[97m{self.health}\x1b[0m\x1b[0m   \x1b[0m")
        print("\x1b[48;5;0m|                       |\x1b[0m")
        print("--------------------------")

Creator = Character("Creator", "Dev")
Creator.show_info()

Evil_Sorcerer = Character("v0id", "Spell Caster")
Evil_Sorcerer.show_info()















id_file = open("id_file.txt", "w")
for line in used_ids:
    id_file.write(str(line) + '\n')
id_file.close()