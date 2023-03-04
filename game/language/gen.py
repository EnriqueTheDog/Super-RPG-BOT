""""
From here you can generate every sort of naming and language items
"""
from langclasses import Gender
from langclasses import ItemType
from langclasses import Name
import random


# TODO: maybe weapon names should also be Name type? Not Persona because we already have persona gender
def random_gender() -> Gender:
    return Gender(random.randint(1, 3))


def random_item_type() -> ItemType:
    return ItemType(random.randint(1, 4))


def persona_name(gender: Gender) -> str:
    return 'JUNARDA' if gender == Gender.FEMININE else 'JUNARDO' if gender == Gender.MASCULINE else 'JUNARDE'


def persona_race(gender: Gender) -> str:
    return 'humana' if gender == Gender.FEMININE else 'humano' if gender == Gender.MASCULINE else 'humane'


def persona_class(gender: Gender) -> str:
    return 'guerrera' if gender == Gender.FEMININE else 'guerrero' if gender == Gender.MASCULINE else 'guerrere'


def item_name(item_type: ItemType) -> str:
    if item_type == ItemType.MELEE:
        return 'hacha'
    if item_type == ItemType.RANGED:
        return 'arco'
    if item_type == ItemType.MAGIC:
        return 'báculo'
    if item_type == ItemType.SACRED:
        return 'mitra'
    return 'cosa'


def mob_name() -> Name:
    name = Name()
    name.gender = Gender.NEUTRAL
    name.string = "esquelete"
    return name
