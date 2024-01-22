from board import *
from pieces import *

board = Board()

for i in range (1,58,8):
	board.squares[i].piece = Pawn(True, i)
for j in range (6,63,8):
	board.squares[j].piece = Pawn(False, i)
board.squares[7].piece = Rook(False, 7)
board.squares[63].piece = Rook(False, 63)
board.squares[15].piece = Knight(False, 15)
board.squares[55].piece = Knight(False, 55)
board.squares[23].piece = Bishop(False, 23)
board.squares[47].piece = Bishop(False, 47)
board.squares[31].piece = Queen(False, 31)
board.squares[39].piece = King(False, 39)
board.squares[0].piece = Rook(True, 0)
board.squares[56].piece = Rook(True, 56)
board.squares[8].piece = Knight(True, 8)
board.squares[48].piece = Knight(True, 48)
board.squares[16].piece = Bishop(True, 16)
board.squares[40].piece = Bishop(True, 40)
board.squares[24].piece = Queen(True, 24)
board.squares[32].piece = King(True, 32)

for m in range(0,64):
	board.squares[i].get_nearest_pieces(board)
	print("Square " + str(m) + "\n")	
	print(board.squares[m].white_moves)
	print(board.squares[m].black_moves)
	print("\n")
