import random

from game.language.langclasses import ItemType
from game.language import gen
from game.numerics.num_helpers import divide


class Item(object):
    # TODO: change item stats through a level param in constructor
    def __init__(self):
        self.variability = None
        self.base_power = None
        self.value = None
        self.type: ItemType = gen.random_item_type()
        self.name: str = gen.item_name(self.type)
        self.lvl: int = 3
        self.strength_bonus: int = 0
        self.dexterity_bonus: int = 0
        self.knowledge_bonus: int = 0
        self.faith_bonus: int = 0
        self.health_bonus: int = 0
        self.vitality_bonus: int = 0
        self.endurance_bonus: int = 0
        self.cardio_bonus: int = 0
        self.intelligence_bonus: int = 0
        self.focus_bonus: int = 0
        self.calculate_stats()
        self.calculate_bonuses()

    def calculate_stats(self):
        perc = divide(self.lvl, 50, 100)
        self.base_power = perc[0]
        self.variability = perc[1] * 2

    def calculate_bonuses(self):
        if random.randint(1, 100) <= self.lvl:
            self.apply_bonus(100)
        if random.randint(33, 100) <= self.lvl:
            self.apply_bonus(66)
        if random.randint(66, 100) <= self.lvl:
            self.apply_bonus(33)

    def calculate_value(self):
        statistics: int = self.lvl
        statistics += self.strength_bonus
        statistics += self.dexterity_bonus
        statistics += self.knowledge_bonus
        statistics += self.faith_bonus
        statistics += self.health_bonus
        statistics += self.endurance_bonus
        statistics += self.vitality_bonus
        statistics += self.cardio_bonus
        statistics += self.intelligence_bonus
        statistics += self.focus_bonus

        value: int = statistics * 99

    def apply_bonus(self, lvl_cut: int):
        select: int = random.randint(0, 9)
        lvl_total = round(self.lvl * lvl_cut / 100)
        amount: int = random.randint(
                self.lvl - round(self.lvl/2),
                self.lvl + round(self.lvl/2)
            )
        if amount < 0:
            amount = 1
        if amount > 100:
            amount = amount - round((amount - 100)/10)
        if select == 0:
            self.strength_bonus += amount
        if select == 1:
            self.dexterity_bonus += amount
        if select == 2:
            self.intelligence_bonus += amount
        if select == 3:
            self.health_bonus += amount
        if select == 4:
            self.faith_bonus += amount
        if select == 5:
            self.endurance_bonus += amount
        if select == 6:
            self.vitality_bonus += amount
        if select == 7:
            self.cardio_bonus += amount
        if select == 8:
            self.intelligence_bonus += amount
        if select == 9:
            self.focus_bonus += amount

    def get_damage_printable(self) -> str:
        return str(self.base_power) + '-' + str(self.base_power + self.variability)

    def get_damage(self) -> int:
        return random.randint(self.base_power, self.base_power + self.variability)
