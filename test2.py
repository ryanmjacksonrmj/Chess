from pieces import *
from board import *
from ascii import *

board = Board()
board.new_game()

board.update_moves()

board.ascii.draw_board(board)


board.squares[35].piece = board.squares[33].piece
board.squares[33].piece = None
board.update_moves()

board.ascii.draw_board(board)