import breeds
class Dev:
    pass
class Magic:
    breeds.Hunter.defense = 0
    breeds.SoundBender.defense = 0
    breeds.Rifleman.defense = 0
    breeds.Brawler.defense = 0
class Deadeye:
    breeds.Rifleman.attack + 5
class CombatKing:
    breeds.Brawler.attack + 2
    breeds.Brawler.defense + 2
class Survivalist:
    breeds.Hunter.defense + 5
class Lullaby:
    breeds.Hunter.defense - 3
    breeds.SpellCaster.defense - 3
    breeds.Rifleman.defense - 3
    breeds.Brawler.defense - 3


