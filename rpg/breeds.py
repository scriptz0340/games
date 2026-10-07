import core_abilities
import auras

class Dev:
    core_ability = core_abilities.Dev()
    aura = auras.Dev()
    attack = 1000
    defense = 1000
class SpellCaster:
    core_ability = core_abilities.Magic()
    aura = auras.Mystery()  
    attack = 5
    defense = 3
class Hunter:
    core_ability = core_abilities.Survivalist()
    aura = auras.Rugged()  
    attack = 5
    defense = 3
class Brawler:
    core_ability = core_abilities.CombatKing()
    aura = auras.BattleWorn()  
    attack = 5
    defense = 3
class Rifleman:
    core_ability = core_abilities.Deadeye()
    aura = auras.Bang()
    attack = 5
    defense = 3
class SoundBender:
    core_ability = core_abilities.Lullaby()
    aura = auras.Tranquil()  
    attack = 5
    defense = 3
