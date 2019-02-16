from hg_conway import Board
from hg_conway.structures import STRUCTURES


class StructureUI:
    """Conway game of live structures.
    """

    def __init__(self, char_set="x", char_unset="."):
        self.char_set = char_set
        self.char_unset = char_unset

    def list(self):
        """List available structures."""
        return "Awailable structures: " + " ".join(STRUCTURES.keys())

    def show(self, name):
        """Show structure."""
        structure = STRUCTURES[name]
        b = Board(structure, char_set=self.char_set, char_unset=self.char_unset)
        return str(b)


def main(args=None):
    import fire

    fire.Fire(StructureUI, args, name="conway")
