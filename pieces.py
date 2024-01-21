class Piece:
	moved_yet = False
	attack_squares = set()
	def __init__(self, white, square_on):
		self.white = white
		self.square_on = square_on

	def vertical_movement(self, square_on):
		lower = (square_on // 8) * 8
		upper = lower + 7
		for entity in range(lower, upper + 1):
			if entity != square_on:
				self.attack_squares.add(entity)

	def horizontal_movement(self, square_on):
		for i in range(square_on % 8, 64, 8):
			if i != square_on:
				self.attack_squares.add(i)

	def diagonal_movement(self, square_on):
		lower = square_on - 9 * (min((square_on % 8), square_on // 8))
		upper= square_on + 9 * ((min(8 - (square_on % 8), 8 - (square_on // 8))) -1)
		for i in range(lower, upper + 1, 8):
			if i != square_on:
				self.attack_squares.add(i)

class Pawn(Piece):
	onlyMovesOne = True

	pass


class Rook(Piece):
	pass

class Knight(Piece):
	pass

class Bishop(Piece):
	pass

class Queen(Piece):
	pass

class King(Piece):
	pass

class Player:
	def __init__(self, white):
		self.white = white


class Board:

	squares = {}
	for key in range (0,64):
		squares[key] = None

	occupied = set()

	def __init__(self):
		pass