from game.language import gen
from game.language.langclasses import Gender
from game.language.langclasses import ItemType
from game.numerics.num_helpers import expo
import item


class Persona(object):
    # TODO: add owner_id from a creator param
    # constructor
    def __init__(self):
        self.owner_id: int = 1
        self.gender: Gender = gen.random_gender()
        self.name: str = gen.persona_name(self.gender)
        self.race: str = gen.persona_race(self.gender)
        self.persona_class: str = gen.persona_class(self.gender)
        self.kills: int = 0
        self.strength: int = 3
        self.dexterity: int = 1
        self.knowledge: int = 1
        self.faith: int = 1
        self.health: int = 100
        self.vitality: int = 1
        self.endurance: int = 100
        self.cardio: int = 0
        self.intelligence: int = 1
        self.focus: int = 1
        self.hp: int = self.health
        self.stamina: int = self.endurance
        self.mana: int = self.intelligence
        self.right_item: item = None
        self.left_item: item = None
        self.is_left_handed: bool = False
        self.is_ambidextrous: bool = False

    def get_stat_by_type(self, stat_type: ItemType) -> int:
        if stat_type == ItemType.MELEE:
            return self.strength
        if stat_type == ItemType.MAGIC:
            return self.knowledge
        if stat_type == ItemType.RANGED:
            return self.dexterity
        if stat_type == ItemType.SACRED:
            return self.faith

    def attack(self, attack_type: ItemType, is_left: bool) -> int:
        """
        returns damage value dealt by player
        """
        current_stat = self.get_stat_by_type(attack_type)
        if is_left:
            if self.left_item is not None and self.left_item.type == attack_type:
                damage = get_damage(current_stat, self.left_item)
            else:
                damage = expo(round(current_stat / 2), 0)
            return damage if self.is_left_handed or self.is_ambidextrous else damage * 0.5
        if not is_left:
            if self.right_item is not None and self.right_item.type == attack_type:
                damage = get_damage(current_stat, self.right_item)
            else:
                damage = expo(round(current_stat / 2), 0)
            return damage if not self.is_left_handed or self.is_ambidextrous else damage * 0.5


def get_damage(stat, current_item: item):
    damage = current_item.get_damage()
    if stat < current_item.lvl:
        damage -= expo(current_item.lvl - stat, -15)
    if stat > current_item.lvl:
        damage += expo(stat - current_item.lvl, 10)
    return damage
