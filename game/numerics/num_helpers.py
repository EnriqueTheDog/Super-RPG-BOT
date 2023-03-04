"""
this is for stats calculus
"""
import game_config
import random


def expo(value: int, grade: int) -> int:
    """
    The base exponential calculus for the game.
    Every variable should pass through here
    Value is for the base number of the calculus (f.e. character lever)
    Grade is the strength of the exponentiation - a higher value here means a slower growing
        a 0 grade means base grade (used for player damage) negative or positive integers are allowed
    """
    return value ** game_config.EXP_POWER / (game_config.EXP_GRADE + grade) + game_config.EXP_GROUND


def divide(base: int, min_percentage: int, max_percentage: int) -> [int]:
    perc: int = random.randint(min_percentage, max_percentage)
    value_1 = round(base * perc / 100)
    value_2 = round(base * (100 - perc) / 100)
    return [value_1, value_2]