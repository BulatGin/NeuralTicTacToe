import random

import rendering
from model import get_model
from tools import Character, commands


class Game:
    model = get_model()

    def __init__(self):
        self.run = False
        self.field = None
        self.character = None
        self.turn = None

    def start(self):
        self.run = True
        self.field = [Character.BLANK for i in range(9)]
        self.character = Character.get_random()
        rendering.hello(Character.get_opposite(self.character))
        rendering.print_field(self.field)

        # first step
        if self.character == Character.CROSS:
            self.turn = True
        else:
            self.turn = False

        while self.run:
            if self.turn:
                step = Game.calculate_step(self.field)
                self.field[step] = self.character
                self.turn = False
            else:
                try:
                    command = commands[input()]
                    self.field[command] = Character.get_opposite(self.character)
                    self.turn = True
                except KeyError:
                    print('Command is unrecognizable')

            rendering.print_field(self.field)

            if self.is_field_full():
                self.run = False

    @staticmethod
    def calculate_step(field) -> int:
        possible_steps = []
        for i in range(len(field)):
            if field[i] == Character.BLANK:
                possible_steps = i

        # TODO
        # dummy choice
        return random.choice(possible_steps)

    def is_field_full(self):
        is_full = True
        for char in self.field:
            is_full &= char != Character.BLANK
        return is_full


if __name__ == '__main__':
    Game().start()
