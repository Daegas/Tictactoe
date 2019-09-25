# Tictactoe

Game player vs. machine
The player always starts, option to choose between 'X' or 'O'
Then the machine uses alpha beta algorithm to choose its next move. 
The leaves have values:
 * 1 when the machine wins
 * 0 when it is draw
 *-1 when the player wins
 
 Based on a list score which contains all the possible moves and the evaluation of the algorithm with this particular move, the machine chooses the most convenient move.
 
 The game is contained in the function play()
