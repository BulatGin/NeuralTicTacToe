from tools import Character


def hello(user_character):
    print('Hello to TicTacToe!\nYou are playing with {}'.format(user_character.value))
    print('All commands must look like \'xx\', where first character may be (t)op, (m)iddle or (b)ottom\n'
          ', second character is (l)eft, (m)iddle, or (r)ight')
    print('Good luck!')


def print_field(field):
    print('|'.join(Character.to_string(field[:3])))
    print('|'.join(Character.to_string(field[3:6])))
    print('|'.join(Character.to_string(field[6:])))
    print('---')
