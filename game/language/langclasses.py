"""
basic classes for language
"""
from enum import Enum


# class syntax
class Gender(Enum):
    NEUTRAL = 1
    FEMININE = 2
    MASCULINE = 3


class ItemType(Enum):
    MELEE = 1
    RANGED = 2
    MAGIC = 3
    SACRED = 4


class Name(object):
    def __init__(self):
        self.gender: Gender = Gender.NEUTRAL
        self.string: str = "name"
