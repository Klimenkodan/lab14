from linkedbst import LinkedBST
from random import choice
from copy import copy
from bstnode import BSTNode
FIRST_PLAYER = 1
COMPUTER = 2
DRAW = 0
NOTHING = -1


class Board:
    def __init__(self):
        self._field = [[None, None, None], [None, None, None], [None, None, None]]
        # field = [['O', None, 'O'], [None, 'O', None], [None, None, 'X']]
        self.last_turn = None

    def status(self, other=None):
        if other is not None:
            field = other
        else:
            field = self._field

        if field[0].count('X') == 3 or field[1].count('X') == 3\
            or field[2].count('X') == 3 or field[0][0] ==\
            field[1][1] == field[2][2] == 'X' or field[0][2] ==\
            field[1][1] == field[2][0] == 'X' or field[0][0] ==\
            field[1][0] == field[2][0] == 'X' or field[0][1] ==\
            field[1][1] == field[2][1] == 'X' or field[0][2] ==\
            field[1][2] == field[2][2] == 'X':
            return FIRST_PLAYER

        elif field[0].count('O') == 3 or field[1].count('O') == 3\
            or field[2].count('O') == 3 or field[0][0] ==\
            field[1][1] == field[2][2] == 'O' or field[0][2] ==\
            field[1][1] == field[2][0] == 'O' or field[0][0] ==\
            field[1][0] == field[2][0] == 'O' or field[0][1] ==\
            field[1][1] == field[2][1] == 'O' or field[0][2] ==\
            field[1][2] == field[2][2] == 'O':
            return COMPUTER

        for row in self._field:
            for cell in row:
                if cell is None:
                    return NOTHING
            return DRAW

    @staticmethod
    def possible_cells(field):
        pos_cells = set()
        for row_index in range(len(field)):
            for element_index in range(len(field[row_index])):
                if field[row_index][element_index] is None:
                    pos_cells.add((row_index, element_index))

        return pos_cells

    def computer_logic(self, data):

        def recurse(tree, field):
            if self.status(field) == NOTHING:
                pass
            elif self.status(field) == COMPUTER:
                pass

            elif self.status(field) == FIRST_PLAYER:
                pass

            else:
                pass

        def making_tree(field):
            node = BSTNode(field)
            field1 = copy(field)
            field2 = copy(field)
            if self.status(field) == NOTHING:
                cell = choice(Board.possible_cells(field))
                cell2 = choice(Board.possible_cells(field))
                field1.turn(cell)
                field2.turn(cell2)
                node.left = making_tree(field1)
                node.right = making_tree(field2)

                return node




        field1 = self._field
        tree = LinkedBST()
        tree.add(field1)
        return recurse(field1)

    def making_tree(self):
        node = BSTNode(self._field)
        field1 = copy(self._field)
        field2 = copy(self._field)
        if self.status() == NOTHING:
            cell = choice(Board.possible_cells(self._field))
            cell2 = choice(Board.possible_cells(self._field))
            field1.turn(cell)
            field2.turn(cell2)
            node.left = self.making_tree(field1)
            node.right = self..making_tree(field2)

            return node

    def is_correct(self, data):
        if 0 > data[0] or data[0] > 2 or 0 > data[1] or data[1] > 2 \
                or self._field[data[0]][data[1]] is not None:
            return False
        else:
            return True

    def turn(self, cell, users_sign):

        if self.is_correct(cell):
            self.last_turn = (cell, users_sign)
            self._field[cell[0]][cell[1]] = users_sign
        else:
            raise IndexError

    def __str__(self):
        str_game = ''
        for row in self._field:
            for element in row:
                str_game += '|' + (element if element is not None else ' ')
            str_game += '|\n'

        return str_game


if __name__ == '__main__':
    bor = Board()
    # bor._field = [[None, None, None], [None, None, None], [None, 'X', 'X']]
    print(bor.status())
    print(bor)
    bor.turn([1, 0], 'X')
    print(bor)
    bor.turn([0, 0], 'X')
    bor.turn([2, 0], 'X')
    print(bor.last_turn)
    print(bor.possible_cells(bor._field))
    tree = bor.making_tree(bor._field)