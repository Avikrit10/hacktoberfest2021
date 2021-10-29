"""Player class and functions

This script contains the Player class and
functions:
    player_turn
    player_position

"""


class Player:
    """
    A class to represent a player

        Attributes:
            name: player's unique name
            position: player position
            dice_sum: most recent dice roll result for player
    """

    def __init__(self, player_name):
        """
        Constructs all necessary attributes for a player object

        :param player_name: string, (name of the player)
        """
        self.name = player_name
        self.position = 0  # Initialised for starting position
        self.dice_sum = 0  # Initialised for no previous dice rolls


def player_turn(turns, players_list):
    """
    determines which player's turn it is

    :param turns: number of turns already played in the game by all
    players combined
    :param players_list: list of all player objects
    :return:
        player object whose turn it is
    """
    player = players_list[turns % len(players_list)]
    return player


def player_position(board_size, dice_sum, player):
    """
    Updates position of the player object and return updated position with player name
    Doesn't let a player go beyond 100

    :param board_size: int, (the size of the board)
    :param dice_sum: int, (the result of dice roll)
    :param player: player object whose turn it is

    :return:
        player_turn.position: int, (updated position)
    """
    curr_position = player.position
    curr_position += int(dice_sum)

    if curr_position <= board_size:
        player.position = curr_position
    else:
        print("Oops, you can not go beyond the Game Board")
    return player.position
