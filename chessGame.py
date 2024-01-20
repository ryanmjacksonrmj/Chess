import chessPieces
import os

black_pawn_one = chessPieces.Pawn(False, (1,7))
black_pawn_two = chessPieces.Pawn(False, (2,7))
black_pawn_three = chessPieces.Pawn(False, (3,7))
black_pawn_four = chessPieces.Pawn(False, (4,7))
black_pawn_five = chessPieces.Pawn(False, (5,7))
black_pawn_six = chessPieces.Pawn(False, (6,7))
black_pawn_seven = chessPieces.Pawn(False, (7,7))
black_pawn_eight = chessPieces.Pawn(False, (8,7))
black_rook_one = chessPieces.Rook(False, (1,8))
black_rook_two = chessPieces.Rook(False, (8,8))
black_knight_one = chessPieces.Rook(False, (2,8))
black_knight_two = chessPieces.Rook(False, (7,8))
black_bishop_one = chessPieces.Rook(False, (3,8))
black_bishop_two = chessPieces.Rook(False, (6,8))
black_queen = chessPieces.Rook(False, (4,8))
black_king = chessPieces.Rook(False, (5,8))
white_pawn_one = chessPieces.Pawn(True, (1,2))
white_pawn_two = chessPieces.Pawn(True, (2,2))
white_pawn_three = chessPieces.Pawn(True, (3,2))
white_pawn_four = chessPieces.Pawn(True, (4,2))
white_pawn_five = chessPieces.Pawn(True, (5,2))
white_pawn_six = chessPieces.Pawn(True, (6,2))
white_pawn_seven = chessPieces.Pawn(True, (7,2))
white_pawn_eight = chessPieces.Pawn(True, (8,2))
white_rook_one = chessPieces.Rook(True, (1,1))
white_rook_two = chessPieces.Rook(True, (8,1))
white_knight_one = chessPieces.Rook(True, (2,1))
white_knight_two = chessPieces.Rook(True, (7,1))
white_bishop_one = chessPieces.Rook(True, (3,1))
white_bishop_two = chessPieces.Rook(True, (6,1))
white_queen = chessPieces.Rook(True, (4,1))
white_king = chessPieces.Rook(True, (5,1))
player_one = chessPieces.Player(True)
player_two = chessPieces.Player(False)
player_one_turn = True
initial_y_values = (1, 2, 7, 8)
occupied_squares = set()
for y in initial_y_values:
	for x in range(1,9):
		occupied_squares.add((x,y))

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
