def check_for_snake(position, snakes_list):
    """
    Checks if the player has encountered any snake from the list of snakes

    :param position: int, (current position of player)
    :param snakes_list: list of snake objects

    :return:
        bool: True if snake encountered, False if not
        snake.snake_end: returns the end position of snake if snake encountered
    """
    if snakes_list:
        for snake in snakes_list:
            if int(snake.snake_start) == int(position):
                return True, int(snake.snake_end)

    return False, 0


def check_for_ladder(position, ladders_list):
    """
    Checks if the player has encountered any ladder from the list of ladders

    :param position: int, (current position of player)
    :param ladders_list: list of ladder objects

    :return:
        bool: True if ladder encountered, False if not
        ladder.ladder_end: returns the end position of ladder if ladder encountered
    """
    if ladders_list:
        for ladder in ladders_list:
            if int(ladder.ladder_start) == int(position):
                return True, int(ladder.ladder_end)

    return False, 0


def position_occupied(position, snakes_list, ladders_list):
    """
    Checks whether the position that the player wants to add a snake/ladder at is already occupied or not

    :param position: position to be checked
    :param snakes_list: list of all snake objects
    :param ladders_list: list of all ladder objects

    :return:
        True if occupied. False if not
    """

    if snakes_list:
        for snake in snakes_list:
            if int(snake.snake_start) == int(position) or int(snake.snake_end) == int(position):
                return True

    if ladders_list:
        for ladder in ladders_list:
            if int(ladder.ladder_start) == int(position) or int(ladder.ladder_end) == int(position):
                return True

    return False
