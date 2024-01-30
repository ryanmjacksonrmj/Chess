from board import *
from pieces import *

board = Board()
board.new_game()

print(board.squares[41].piece.moved_yet)


board.squares[60].piece = board.squares[32].piece
board.squares[32].piece = None

board.squares[60]
