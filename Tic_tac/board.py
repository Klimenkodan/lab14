class Board:
    def __init__(self):
        # self.field = 3 * [3 * [None]]
        self.field = [[None, None, 'X'], [None, None, 'X'], [None, None, 'X']]
        # self.field = field.turn()

    def status(self):
        if self.field[0].count('X') == 3 or self.field[1].count('X') == 3 or self.field[2].count('X') == 3\
        or self.field[0][0] == self.field[1][1] == self.field[2][2] == 'X' or self.field[0][2] == self.field[1][1]\
        == self.field[2][0] == 'X' or self.field[0][0] == self.field[1][0] == self.field[2][0] == 'X' or\
        self.field[0][1] == self.field[1][1] == self.field[2][1] == 'X' or self.field[0][2] == self.field[1][2]\
        == self.field[2][2] == 'X':
            return 1


        else:
            return 0

    def computer_logic(self):
        pass

    def turn(self):

        def is_correct():
            pass

        pass

    def __str__(self):
        pass


if __name__ == '__main__':
    bor = Board()
    # bor.field = [[None, None, None], [None, None, None], [None, 'X', 'X']]
    print(bor.status())