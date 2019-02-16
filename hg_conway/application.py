from hg_conway import Board
from hg_conway.structures import STRUCTURES
from hg_conway.structures.application import StructureUI


class MainUI:
    """Conway's game of life.

    Simple implementation of the game of life.
    """

    def __init__(self, char_set="x", char_unset="."):
        self.char_set = char_set
        self.char_unset = char_unset

        self.structures = StructureUI(char_set, char_unset)

    def play(
        self,
        structure: str,
        interval: float = 0.1,
        steps: int = 100,
        size: int = 20,
        height: int = 50,
        border: bool = True,
    ):
        """Start game of life.

        structure: Name of the starting structure
        interval: Time between evolutions, defaults to 0.1
        steps: Number of evolutions, defaults to 100
        size: Size of game board, defaults to 20
        height: Height of game board, defaults to 50
        border: Limit board to initial dimensions, defaults to True
        """

        b = Board(
            STRUCTURES[structure],
            size=size,
            border=border,
            height=height,
            char_set=self.char_set,
            char_unset=self.char_unset,
        )
        b.run(interval=interval, steps=steps)
        return 0


def main(args=None):
    import fire

    try:
        fire.Fire(MainUI, args, name="conway")
    except KeyboardInterrupt:
        # quit without stack trace
        return 1
