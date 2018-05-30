from tools import Character


def hello(user_character):
    print('Hello to TicTacToe!\nYou are playing with {}'.format(user_character))
    print('All commands must look like \'xx\', where first character may be (t)op, (m)iddle or (b)ottom\n'
          ', second character is (l)eft, (m)iddle, or (r)ight')
    print('Good luck!')


def print_field(field):
    print('|'.join(field[:3]))
    print('|'.join(field[3:6]))
    print('|'.join(field[6:]))
