"""Ladder Class

This script contains the ladder class

"""


class Ladder:
    """
    A  class to represent a ladder

        Attributes
            ladder_start: starting position of ladder object
            ladder_end: ending position of ladder object

            The player should avoid inputting positions that are already occupied
    """

    def __init__(self, ladder_start, ladder_end):
        """
        Constructs all necessary attributes for the ladder object

        :param ladder_start: str
        :param ladder_end: str
        """
        self.ladder_start = ladder_start
        self.ladder_end = ladder_end
