"""Snakes and Ladders Game

This script allows the user to play a round of Snakes and Ladders.

The user can configure the Game Board by setting the number of positions
on the board in the range of 5-100 adding Snakes or Ladders at any
position.

Any number of players can be added to the game.

All the configurations need to be done before starting the game.

A player wins if they reach the last position available on the board before
all other players.

"""


import snake
import ladder
import player
import checks
import board_configuration
import game_flow


if __name__ == '__main__':

    rematch = True
    while rematch:

        print("_________________________________________________________________________")
        print("~~~~~~~~~~~~~~~~~Welcome To A Game of Snakes And Ladders~~~~~~~~~~~~~~~~~")
        print("_________________________________________________________________________")
        player_input = 0
        snakes = []  # list of snake objects
        ladders = []  # list of ladder objects
        players = []  # list of player objects
        player_names = []  # list of unique player names
        winner = "None"  # name of game winner

        board_size: int = 0  # board size: number of available positions

        # taking user input for the board size: the number of positions available on board
        while True:
            try:
                while board_size < 5 or board_size > 100:
                    board_size = int(input("Please enter the preferred board size in the range of 5-100 \n"
                                           "to set the number of playable positions: "))
                break

            except ValueError:
                print('Please enter an INTEGER')

        print(f"The playable positions on the board have been set as 1-{board_size}, \n "
              f"make sure your snake and ladder points are within the range")

        print(f"The player who reaches {board_size} first, WINS  :)")

        # the following code block initialises the game by taking configuration input from the players
        while player_input != "go":
            print("Enter 1 to add a Snake")
            print("Enter 2 to add a Ladder")
            print("Enter 3 to add a Player")
            print("Enter 4 to see the Snakes and Ladders positions")
            print("Enter 'go' to ||~~BEGIN THE GAME~~||")

            player_input = input()

            # the following code block creates a snake instance and appends it in snakes list
            if player_input == "1":

                while True:
                    try:
                        sn_start = int(input("Enter the Starting Point of Snake: "))
                        break

                    except ValueError:
                        print("Please enter an INTEGER")

                # following code block prevents the user from placing a snake at incorrect positions
                while int(sn_start) == board_size or int(sn_start) > board_size or int(sn_start) < 2:

                    if int(sn_start) == board_size:
                        print("Sorry, if there is a Snake at last position, nobody will ever win ;)")
                        while True:
                            try:
                                sn_start = int(input("Enter the Starting Point of Snake: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                    if int(sn_start) > board_size or int(sn_start) < 1:
                        print(f"Please keep the point in range of the board: 1-{board_size}")
                        while True:
                            try:
                                sn_start = int(input("Enter the Starting Point of Snake: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                    if int(sn_start) == 1:
                        print("If you snake STARTS at 1, where will it end?? xD")
                        while True:
                            try:
                                sn_start = int(input("Enter the Starting Point of Snake: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                # following code block checks if the position is already occupied
                while checks.position_occupied(sn_start, snakes, ladders):
                    print("Oops, it seems like this position is already occupied")
                    while True:
                        try:
                            sn_start = int(input("Enter the Starting Point of Snake: "))
                            break

                        except ValueError:
                            print("Please enter an INTEGER")

                while True:
                    try:
                        sn_end = int(input("Enter the Ending Point of Snake: "))
                        break

                    except ValueError:
                        print("Please enter an INTEGER")

                # following code block prevents the user from placing a snake at incorrect positions
                while int(sn_end) >= int(sn_start) or int(sn_end) < 1:
                    if int(sn_end) >= int(sn_start):
                        print(
                            "A Snake's ending point should be lower than "
                            "its starting point, otherwise  what's the point ;)")
                        while True:
                            try:
                                sn_end = int(input("Enter the Ending Point of Snake: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                    if int(sn_end) < 1:
                        print(f"Please keep the point in the range of the board: 1-{board_size}")
                        while True:
                            try:
                                sn_end = int(input("Enter the Ending Point of Snake: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                # following code block checks if the position is already occupied
                while checks.position_occupied(sn_end, snakes, ladders):
                    print("Oops, it seems like this position is already occupied")
                    while True:
                        try:
                            sn_end = int(input("Enter the Ending Point of Snake: "))
                            break

                        except ValueError:
                            print("Please enter an INTEGER")

                # adding snake object to snake list
                sn = snake.Snake(sn_start, sn_end)
                snakes.append(sn)
                print(f"Snake added from |{sn_start}| to |{sn_end}|")

            # the following code block creates a ladder instance and appends it in ladders list
            elif player_input == "2":

                while True:
                    try:
                        ld_start = int(input("Enter the Starting Point of Ladder: "))
                        break

                    except ValueError:
                        print("Please enter an INTEGER")

                # following code block prevents the user from placing a ladder at incorrect positions
                while int(ld_start) == board_size or int(ld_start) > board_size or int(ld_start) < 1:

                    if int(ld_start) == board_size:
                        print("If your ladder STARTS at last position, where will it take the player to?? XD")
                        while True:
                            try:
                                ld_start = int(input("Enter the Starting Point of Ladder: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                    if int(ld_start) > board_size or int(ld_start) < 1:
                        print(f"Please keep the point in range of the board: 1-{board_size}")
                        while True:
                            try:
                                ld_start = int(input("Enter the Starting Point of Ladder: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                # following code block checks if the position is already occupied
                while checks.position_occupied(ld_start, snakes, ladders):
                    print("Oops, it seems like this position is already occupied")
                    while True:
                        try:
                            ld_start = int(input("Enter the Starting Point of Ladder: "))
                            break

                        except ValueError:
                            print("Please enter an INTEGER")

                while True:
                    try:
                        ld_end = int(input("Enter the Ending Point of Ladder: "))
                        break

                    except ValueError:
                        print("Please enter an INTEGER")

                # following code block prevents the user from placing a ladder at incorrect positions
                while int(ld_end) <= int(ld_start) or int(ld_end) > board_size:

                    if int(ld_end) <= int(ld_start):
                        print(
                            "A Ladder's ending point should be higher than "
                            "its starting point, otherwise what's the point ;)")
                        while True:
                            try:
                                ld_end = int(input("Enter the Ending Point of Ladder: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                    if int(ld_end) > board_size:
                        print(f"Please keep the point in range of the board: 1-{board_size}")
                        while True:
                            try:
                                ld_end = int(input("Enter the Ending Point of Ladder: "))
                                break

                            except ValueError:
                                print("Please enter an INTEGER")

                # following code block checks if the position is already occupied
                while checks.position_occupied(ld_end, snakes, ladders):
                    print("Oops, it seems like this position is already occupied")
                    while True:
                        try:
                            ld_end = int(input("Enter the Ending Point of Ladder: "))
                            break

                        except ValueError:
                            print("Please enter an INTEGER")

                # adding ladder object to ladder list
                ld = ladder.Ladder(ld_start, ld_end)
                ladders.append(ld)
                print(f"Ladder added from |{ld_start}| to |{ld_end}|")

            # the following code block creates a player instance and appends it in players list
            elif player_input == "3":
                pl_name = input("Enter a unique name for the player: ")
                pl_name = pl_name.strip()

                # following code block prevents user from inputting invalid or repetitive names
                while pl_name in player_names or pl_name == "":
                    # to ensure unique name for each player
                    if pl_name in player_names:
                        print(f"|{pl_name}| is already in use.")
                        pl_name = input("Enter a UNIQUE name for the player: ")
                        pl_name = pl_name.strip()

                    # to make sure name is not blank
                    if pl_name == "":
                        print(f"|{pl_name}| is hardly a name, at least add ONE LETTER.")
                        pl_name = input("Enter a unique name for the player: ")
                        pl_name = pl_name.strip()

                # adding player object to player list
                player_names.append(pl_name)
                pl = player.Player(pl_name)
                players.append(pl)

            # the following code block calls display_board function to display the board configuration
            elif player_input == "4":
                board_configuration.display_configuration(snakes, ladders)

            # the following code block starts the game by calling the play_game function and ends the current
            # while loop if user has added min 2 players to the game
            elif player_input == "go":
                if len(players) > 1:
                    game_flow.play_game(board_size, winner, snakes, ladders, players)
                else:
                    print("At least add 2 players to play a fair game ;)")
                    player_input = "nope"

        # following code block determines whether there will be a rematch or not
        if input("If you want a REMATCH, enter 'yes': ") == "yes":
            continue
        else:
            print("Well, that does not look like a yes. Thank you for playing. :)")
            input("Enter anything to quit the console")
            rematch = False
