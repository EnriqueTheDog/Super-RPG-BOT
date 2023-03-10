import random

from game.language.langclasses import Name
from game.numerics.num_helpers import divide
from game.numerics.num_helpers import expo
from game.language import gen
from random import randint


class Mob(object):
    # TODO: externalise level in constructor and extract mob grade to config
    def __init__(self, lvl: int):
        self.lvl = expo(lvl, -2)
        self.name: Name = gen.mob_name()
        perc: [int] = divide(self.lvl, 50, 80)
        self.damage = perc[0]
        self.hp = perc[1] * 30
        damage_perc: [int] = divide(self.damage, 50, 100)
        self.base_damage: int = damage_perc[0]
        self.var_damage: int = damage_perc[1] * 2

    def attack(self) -> int:
        """
        returns damage dealt by the mob
        """
        return self.base_damage + randint(0, self.var_damage)