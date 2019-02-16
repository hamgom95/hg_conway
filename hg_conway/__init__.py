"""
Implementation of Conway's Game of Life
"""

__all__ = ["neighbors", "Board"]

import sys
import time
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def neighbors(cell, distance=1):
    """Return the neighbors of cell."""
    x, y = cell
    r = range(0 - distance, 1 + distance)
    return (
        (x + i, y + j)  # new cell offset from center
        for i in r
        for j in r  # iterate over range in 2d
        if not i == j == 0
    )  # exclude the center cell


class Board(object):
    """Conways game of life board"""

    def __init__(
        self,
        board=set(),
        *,
        border=True,
        size=None,
        height=None,
        width=None,
        char_set="x",
        char_unset=".",
        char_sep=" "
    ):
        self.board = board

        size = 0 if size is None else size
        self.height = size if height is None else height
        self.width = size if width is None else width

        self.border = border

        self.char_set = char_set
        self.char_unset = char_unset
        self.char_sep = char_sep

    def __iter__(self):
        """advance board"""
        while True:
            self.advance()
            yield self.board

    def constrain(self):
        """constrain objects on board"""
        self.board = set(cell for cell in self.board if cell[0] <= self.width and cell[1] <= self.height)

    def advance(self):
        new_board = set()
        for cell in self.board:
            cell_neighbors = set(neighbors(cell))
            # test if live cell dies
            if len(self.board & cell_neighbors) in [2, 3]:
                new_board.add(cell)
            # test dead neighbors to see if alive
            for n in cell_neighbors:
                if len(self.board & set(neighbors(n))) is 3:
                    new_board.add(n)
        self.board = new_board

        if self.border:
            self.constrain()

    def state(self):
        sizex = self.height
        sizey = self.width

        for x, y in self.board:
            sizex = x if x > sizex else sizex
            sizey = y if y > sizey else sizey

        board_mat = [[(i, j) in self.board for i in range(sizex + 1)] for j in range(sizey + 1)]
        return board_mat

    def __str__(self):
        board_bool = self.state()
        board_char = [[self.char_set if i else self.char_unset for i in l] for l in board_bool]
        board_str = "\n".join([self.char_sep.join(l) for l in board_char])
        return board_str

    def run(self, steps=None, *, interval=0.1, info=True):
        """Generator to create new evolutions of game board."""
        for cnt, board in enumerate(self):
            if cnt == steps:
                break

            sys.stdout.write("\033[H")  # move to the top
            sys.stdout.write("\033[2J")  # clear the screen

            if info:
                print("step: {}" if steps is None else "step: {} / {}".format(cnt, steps))

            print(str(self))

            time.sleep(interval)
