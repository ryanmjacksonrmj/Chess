from pieces import *
from board import *
from ascii import *
from os import system, name
import time

#need to fix knight moves and make it so it doesn't change players if an invalid move for a piece is picked

def clear():
    # for windows
    if name == 'nt':
      system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
      system('clear')

def turn(board, last_move):
  while True:
    clear()
    if last_move is not None: print(last_move)
    print("\n\n")
    board.update_moves()
    if board.white_to_move == True:
      print("White's turn to move.\n\n")
      current_player = "White"
      opposing_player = "Black"
    else:
      print("Black's turn to move.\n\n")
      current_player = "Black"
      opposing_player = "White"
    board.ascii.draw_board(board)
    print("Enter ? for a list of commands or enter your move (e.g. 'move e7 to e5' or 'move g8 to f6').")
    user_input = input()
    if user_input == "?":
      print("List of commands\n\n'?' for a list of commands\n'q' quits to the menu\n'draw' to request a draw\n'resign' to resign\n'save' to save the current state of the board\n'undo' to request an undo of the last move\n'board' to view the board\n'move' (e.g. 'move e7 to e5')\n")
    elif user_input == "q":
      return "break"
    elif user_input == "resign":
      while True:
        print("Are you sure you want to resign? (y/n)")
        resignation = input()
        if resignation == "y":
          print(current_player + " has resigned. " + opposing_player + " wins!")
          time.sleep(3)
          return "break"
        if resignation == "n":
          pass
    elif user_input == "draw":
      pass
    elif user_input == "save":
      pass
    elif user_input == "undo":
      pass
    elif user_input == "board":
      board.ascii.draw_board(board)
    elif user_input.startswith("move ") and len(user_input) == 13 and user_input[5:7] in board.algebraic_squares and user_input[11:13] in board.algebraic_squares:
      from_square = user_input[5:7]
      to_square = user_input[11:13]
      from_square_number = convert_to_square_number(from_square)
      to_square_number = convert_to_square_number(to_square)
      print(board.squares[from_square_number].piece)
      print(board.squares[to_square_number].piece)
      print(board.squares[from_square_number].piece_moves)
      time.sleep(3)
      if board.squares[from_square_number].piece.is_white == board.white_to_move:
        board.squares[from_square_number].get_piece_moves(board)
        print("Same color piece")
        time.sleep(3)
        if to_square_number in board.squares[from_square_number].piece_moves:
          move_pieces(board, from_square_number, to_square_number)
          print("Is white to move?")
          print(board.white_to_move)
          time.sleep(3)
          break
        else:
          print("Invalid move! Please choose another.")
          time.sleep(3)
      else:
        print("It is " + current_player + "'s turn to move!")
        time.sleep(3)
    else:
      print("Invalid entry! Try another command. Enter ? for a list of commands.")
      time.sleep(3)

def move_pieces(board, from_square_number, to_square_number):
  board.squares[to_square_number].piece = board.squares[from_square_number].piece
  board.squares[from_square_number].piece = None
  board.squares[to_square_number].piece.moved_yet == True

def convert_to_square_number(square):
  columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  rows = ['8', '7', '6', '5', '4', '3', '2', '1']
  columns_index = columns.index(square[0])
  rows_index = rows.index(square[1])
  square_number = rows_index + (8 * columns_index)
  return square_number

def new_game():
  board = Board()
  board.new_game()
  last_move = None
  while True:
    last_move = turn(board, last_move)
    board.white_to_move = not board.white_to_move
    if last_move == "break":
      return

def title_screen():
   while True:
    clear()
    print("Terminal Chess!\n")
    print("1. Start a New Game\n")
    print("2. Continue Your Last Game\n")
    print("3. Exit\n\n")
    selection = input("Enter your selection: ")
    match selection:
        case "1":
          new_game()

        case "2":
          pass    

        case "3":
          break

title_screen()