from board import *

board = Board()
for i in board.squares:
	print ("Square " + str(board.squares[i].number) + ": ")
	print (board.squares[i].squares_diagonal_backward_left)
