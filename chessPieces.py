class Piece:
	jumpPieces = False
	movedYet = False
	lastMoved = False
	onlyMovesOne = False
	onBoard = True
	
	def __init__(self, white, occupying_square):
		self.white = white
		self.occupying_square = occupying_square

	def pathClear():
		pass

	def move(self, occupying_square):
		if movingCorrectly and pathClear and spaceEmpty:
			self.occupying_square = occupying_square

	def take(self, occupying_square):
		if movingCorrectly and pathClear and spaceOccupied and oppositeColor and notKing:	
				pass
		
	def reportPosition(self):
		position = (self.name, self.occupying_square)
		return position

class Pawn(Piece):
	canMoveTwo = True
	onlyMovesOne = True
	takesDiagonal = True

	pass


class Rook(Piece):
	pass

class Knight(Piece):
	jumpPieces = True
	pass

class Bishop(Piece):
	pass

class Queen(Piece):
	pass

class King(Piece):
	onlyMovesOne = True
	pass

class Board:
	occupied = {}

	def update():
		pass

class Player:
	def __init__(self, white):
		self.white = white