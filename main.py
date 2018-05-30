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
                step = Game.calculate_step(self.field, self.character)
                self.field[step] = self.character
                print('The Great Mind makes its move')
                self.turn = False
            else:
                try:
                    command = commands[input()]
                    if self.field[command] == Character.BLANK:
                        self.field[command] = Character.get_opposite(self.character)
                        self.turn = True
                    else:
                        print('Field is already occupied')
                except KeyError:
                    print('Command is unrecognizable')

            rendering.print_field(self.field)

            if self.is_game_completed():
                if self.turn:
                    print("Wow! You are a winner of AI!")
                else:
                    print("Haha! AI is a winner)")
                print("The end")
                self.run = False

            if self.is_field_full():
                print("The field is full(((")
                self.run = False

    @staticmethod
    def calculate_step(field, char) -> int:
        possible_steps = []
        for i in range(len(field)):
            if field[i] == Character.BLANK:
                possible_steps.append(i)

        best_step = (0, 0)  # (step, probability)
        for step in possible_steps:
            field_copy = field.copy()
            field_copy[step] = char
            encoded_field_copy = Character.multiple_encode(field_copy)
            proba = Game.model.predict_proba([encoded_field_copy])
            probability = proba[0][1] if char == Character.CROSS else proba[0][0]
            if probability > best_step[1]:
                best_step = (step, probability)

        return best_step[0]

    def is_field_full(self):
        is_full = True
        for char in self.field:
            is_full &= char != Character.BLANK
        return is_full

    @staticmethod
    def check_win_combination(*combinations):
        for char in combinations:
            if char != combinations[0] or char == Character.BLANK:
                return False
        return True

    def is_game_completed(self):
        return Game.check_win_combination(*self.field[:3]) or \
               Game.check_win_combination(*self.field[3:6]) or \
               Game.check_win_combination(*self.field[6:]) or \
               Game.check_win_combination(self.field[0], self.field[3], self.field[6]) or \
               Game.check_win_combination(self.field[1], self.field[4], self.field[7]) or \
               Game.check_win_combination(self.field[2], self.field[5], self.field[8]) or \
               Game.check_win_combination(self.field[0], self.field[4], self.field[8]) or \
               Game.check_win_combination(self.field[2], self.field[4], self.field[6])



if __name__ == '__main__':
    Game().start()
