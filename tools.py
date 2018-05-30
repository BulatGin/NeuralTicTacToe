import random
from enum import Enum

commands = {
    'tl': 0,
    'tm': 1,
    'tr': 2,
    'ml': 3,
    'mm': 4,
    'mr': 5,
    'bl': 6,
    'bm': 7,
    'br': 8
}


class Character(Enum):
    CROSS = 'X'
    ZERO = 'O'
    BLANK = ' '

    @staticmethod
    def get_random():
        if random.randint(0, 1) == 0:
            return Character.CROSS
        else:
            return Character.ZERO

    @staticmethod
    def get_opposite(c):
        if c == Character.ZERO:
            return Character.CROSS
        elif c == Character.CROSS:
            return Character.ZERO
        else:
            raise KeyError

    @staticmethod
    def encode(char):
        if char == Character.CROSS:
            return [0, 0, 1]
        elif char == Character.ZERO:
            return [0, 1, 0]
        elif char == Character.BLANK:
            return [1, 0, 0]
        else:
            raise KeyError

    @staticmethod
    def multiple_encode(l):
        result = []
        for char in l:
            result.extend(Character.encode(char))
        return result
