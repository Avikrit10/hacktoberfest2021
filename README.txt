Hi, following is a quick run through of game play:


*The game asks for board size:
	-board size refers to how many positions will be available on the board
	-the size should be in range 5-100 (100 included)

*The game will confirm the range of available positions

*The player that reaches the LAST position before others, WINS

*The Game provides 5 options to go ahead
	1: Add snakes
	2: Add ladders
	3: Add players
	4: View snakes and ladder positions
	5: Start the game

*Add snakes:
	rules for snake start point:
		-should not be last position
		-should be within the range of positions on board
		-should not be 1
		-should not be already occupied

	rules for snake end point:
		-should not be higher than snake start position
		-should be within the range of positions on board
		-should not be already occupied

*Add ladders:
	rules for ladder start point:
		-should not be last position
		-should be within the range of positions on board
		-should not be already occupied

	rules for ladder end point:
		-should not be lower than ladder start position
		-should be within the range of positions on board
		-should not be already occupied

*Add player:
	rules for player names:
		-should be unique
		-should not be blank
	AT LEAST 2 PLAYERS necessary for the game to begin

*View snakes and ladder positions:
	use it to view the positions of snakes and ladders before 
	starting the game

*Start the game:
	ENTER 'go' to start the game

*All players START FROM 0

*There is no concept of getting a necessary 1 or 6 to start moving 
forward

*Once the game starts, each player must press ENTER when their turn 
comes in order to roll the dice and proceed with the game

*Dice roll result is randomly generated

*At each turn, player is informed:
	-dice roll result
	-position after dice roll
	-whether or not any snake/ladder encountered
	-position after snake/ladder encountered (ONLY IF ENCOUNTERED)

*A player cannot go beyond the board, they must wait for next chance if
dice roll result is more than required number

*If a player rolls a 6, they are given another chance and the result gets added
This only happens TWICE. If 6 is rolled for a THIRD time, the player does not
move forward for that chance.

*When a player reaches the last position, they WIN.

*At the end of the game, user is asked if they wish to have a REMATCH
	-if user inputs 'yes', games starts all over again with 
	-when game restarts, all previous configurations are ERASED
	-if user inputs anything else, the game ends 
	-user can enter anything to close the console
 
	