from board import *
from pieces import *

board = Board()
board.new_game()

board.update_moves()

#For now this is just printing off all of the 
for square in board.squares:
	print(board.squares[square].piece_moves)