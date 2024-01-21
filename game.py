from pieces import *
import os

Board.squares[6] = black_pawn_one = Pawn(False, 7)
Board.squares[14] = black_pawn_two = Pawn(False, 15)
Board.squares[22] = black_pawn_three = Pawn(False, 23)
Board.squares[30] = black_pawn_four = Pawn(False, 31)
Board.squares[38] = black_pawn_five = Pawn(False, 39)
Board.squares[46] = black_pawn_six = Pawn(False, 47)
Board.squares[54] = black_pawn_seven = Pawn(False, 55)
Board.squares[62] = black_pawn_eight = Pawn(False, 63)
Board.squares[7] = black_rook_one = Rook(False, 8)
Board.squares[63] = black_rook_two = Rook(False, 64)
Board.squares[15] = black_knight_one = Knight(False, 16)
Board.squares[55] = black_knight_two = Knight(False, 56)
Board.squares[23] = black_bishop_one = Bishop(False, 24)
Board.squares[47] = black_bishop_two = Bishop(False, 48)
Board.squares[31] = black_queen = Queen(False, 32)
Board.squares[39] = black_king = King(False, 40)
Board.squares[1] = white_pawn_one = Pawn(True, 2)
Board.squares[9] = white_pawn_two = Pawn(True, 10)
Board.squares[17] = white_pawn_three = Pawn(True, 18)
Board.squares[25] = white_pawn_four = Pawn(True, 26)
Board.squares[33] = white_pawn_five = Pawn(True, 34)
Board.squares[41] = white_pawn_six = Pawn(True, 42)
Board.squares[49] = white_pawn_seven = Pawn(True, 50)
Board.squares[57] = white_pawn_eight = Pawn(True, 58)
Board.squares[0] = white_rook_one = Rook(True, 1)
Board.squares[56] = white_rook_two = Rook(True, 57)
Board.squares[8] = white_knight_one = Knight(True, 9)
Board.squares[48] = white_knight_two = Knight(True, 49)
Board.squares[16] = white_bishop_one = Bishop(True, 17)
Board.squares[40] = white_bishop_two = Bishop(True, 41)
Board.squares[24] = white_queen = Queen(True, 25)
Board.squares[32] = white_king = King(True, 33)
for key, value in Board.squares:
	if value != None:
		Board.occupied.add(key)


player_one = Player(True)
player_two = Player(False)
player_one_turn = True

def clear_screen():
	#Clears the screen regardless of operating system.
	if os.name == "posix":
		os.system('clear')
	else:
		os.system('cls')

def convert_square(square):
	first_character = ("a", "b", "c", "d", "e", "f", "g", "h")
	second_character = ("1", "2", "3", "4", "5", "6", "7", "8")
	if len(square) != 2:
		x = -1
		y = -1
	elif square[0].lower() not in first_character or square[1] not in second_character:
		x = -1
		y = -1
	else:
		x = ord(square[0].lower()) - 96 #This should convert a letter to the corresponding number a:1 b:2, etc.
		y = int(square[1])
	converted_square = (x,y)
	print (converted_square)
	return converted_square

def new_game():
	clear_screen()
	print("New game\n")
	while True:
		if player_one_turn == True:
			print("White's turn to move.\n\n")
		else:
			print("Black's turn to move.\n\n")
		print("Enter 1 to make a move.\n")
		print("Enter 2 to offer a draw.\n")
		print("Enter 3 to resign.\n")
		user_choice = input("Enter your selection here: ")
		if user_choice == "1":
			turn()
		elif user_choice == "3":
			break

def turn():
	global player_one_turn
	while True:
		starting_space = input("\n\nEnter the space of the piece you want to move.\n")
		starting_space = convert_square(starting_space)
		if starting_space != (-1,-1):
			break
	while True:
		ending_space = input("Enter the space you're moving to.\n")
		ending_space = convert_square(ending_space)
		if ending_space != (-1,-1):
			break
	print (starting_space)
	player_one_turn^= True

while True:
	# Game Loop
	clear_screen()
	print("Chess\n")
	print("Enter 1 to start a new game.\n\nEnter 0 to quit.\n")
	selection = input("Enter your selection here: ")
	if selection == "0":
		break
	elif selection == "1":
		new_game()
