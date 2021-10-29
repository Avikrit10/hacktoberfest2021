"""Board Configuration

This script displays the Board Configuration, i.e,
the position of Snakes and Ladders as placed by
the user
"""


def display_configuration(snakes_list, ladders_list):
    """
    Displays the snakes and ladders configurations set by the user

    :param snakes_list: list of all snake objects
    :param ladders_list: list of all ladder objects

    :return:
        prints the snakes and ladders configurations
    """
    # following code block prints the configuration of all the snakes on the board
    if snakes_list:
        print("__________________________________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~Snakes~~~~~~~~~~~~~~~~~~~~~~")
        print("__________________________________________________")
        for index, _snake in enumerate(snakes_list):
            print(f'Snake No. {index+1}: from |{_snake.snake_start}| to |{_snake.snake_end}|')
    else:
        print("__________________________________________________")
        print("~~~~~~~~~~~~~~~~~~~No Snakes Added~~~~~~~~~~~~~~~~")
        print("__________________________________________________")

    # following code block prints the configuration of all the ladders on the board
    if ladders_list:
        print("__________________________________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~Ladders~~~~~~~~~~~~~~~~~~~~~")
        print("__________________________________________________")
        for index, _ladder in enumerate(ladders_list):
            print(f'Ladder No. {index+1}: from |{_ladder.ladder_start}| to |{_ladder.ladder_end}|')
        print("__________________________________________________")
        print("__________________________________________________")
    else:
        print("__________________________________________________")
        print("~~~~~~~~~~~~~~~No Ladders Added~~~~~~~~~~~~~~~~~~~")
        print("__________________________________________________")
