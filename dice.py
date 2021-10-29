"""DIce Roll

This script returns a random number in the range of
1-6 (6 included) whenever called

It acts as a dice roll result generator
"""


import math
import random


def roll_dice():
    """
    Returns the result of a random dice roll (1-6)

    :return:
        dice_sum: int
    """

    dice_sum = int(math.ceil(random.random() * 6))
    return int(dice_sum)
