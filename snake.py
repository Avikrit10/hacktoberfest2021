"""Snake class

This script contains the snake class
"""


class Snake:
    """
    A  class to represent a snake

        Attributes
            snake_start: starting position of snake object
            snake_end: ending position of snake object

            The player should avoid inputting positions that are already occupied
    """

    def __init__(self, snake_start, snake_end):
        """
        Constructs all necessary attributes for the snake object

        :param snake_start: str
        :param snake_end: str
        """
        self.snake_start = snake_start
        self.snake_end = snake_end
