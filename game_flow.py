"""Game Flow

This script determines the game flow once all the
configurations are taken care of.

The function play_game takes in inputs provided by the user
and runs the script till a winner is declared
"""

import dice
import testing
import player
import checks


def play_game(board_size, game_winner, snakes_list, ladders_list, players_list):
    """
    This function is responsible of calling other functions and attributed whenever required in the
    entirety of the game.
    This is where the game loop occurs until a winner is declared.
    4

    :param board_size: size of the board
    :param game_winner: name of winner, None at the beginning of the game
    :param snakes_list: list of all snake objects
    :param ladders_list: list of all ladder objects
    :param players_list: list of all player objects
    """
    turns = -1  # keeps a count of player turns

    # the following loop continues until a winner is declared
    while game_winner == "None":

        turns += 1

        # which player's chance to roll
        player_playing = player.player_turn(turns, players_list)
        print(f"It is {player_playing.name}'s turn to roll the dice")

        # to check functioning
        testing_feature = input("Hit Enter to roll the dice")
        if testing_feature == "testing":
            num_on_dice = testing.testing_snakes_and_ladders()

        else:
            # dice is rolled by the player whose turn it is
            num_on_dice = dice.roll_dice()

        dice_sum = int(num_on_dice)
        num_of_sixes = 0
        print(f"{player_playing.name} rolled a |{dice_sum}|")

        # special condition for getting a 6
        while int(num_on_dice) == 6:
            num_of_sixes += 1
            if num_of_sixes == 3:
                print("Oops, getting a 6 THREE TIMES makes your turn NULL AND VOID")
                dice_sum = 0
                break
            print("Since you got a 6, roll again")
            testing_feature = input("Hit Enter to roll the dice")
            if testing_feature == "testing":
                num_on_dice = testing.testing_snakes_and_ladders()

            else:
                # dice is rolled by the player whose turn it is
                num_on_dice = dice.roll_dice()
            print(f"{player_playing.name} rolled a |{dice_sum}|")
            dice_sum += int(num_on_dice)

        # after dice roll, player position is updated
        p_pos = player.player_position(board_size, dice_sum, player_playing)
        if p_pos < board_size:
            print(f"Player |{player_playing.name}| has reached |{p_pos}|")

        # reached position is checked for the presence of any snake object
        check_snake, end_point = checks.check_for_snake(p_pos, snakes_list)
        if check_snake:
            player_playing.position = end_point
            print(f"Player |{player_playing.name}| has encountered a SNAKE and fallen to |{end_point}| OOF THAT'S BAD")

        # reached position is checked for the presence of any snake object
        check_ladder, end_point = checks.check_for_ladder(p_pos, ladders_list)
        if check_ladder:
            player_playing.position = end_point
            print(f"Player |{player_playing.name}| has encountered a LADDER and climbed to |{end_point}| "
                  "YAY GOOD FOR YOU")

        # reached position is checked for game winning condition (reaching 100 or beyond)
        if p_pos == board_size:
            game_winner = player_playing.name
            print(f"Player ||~~{game_winner}~~|| has WON")

        print("_________________________________________________________")
