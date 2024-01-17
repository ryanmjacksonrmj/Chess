class Piece:
	jumpPieces = False
	movedYet = False
	lastMoved = False
	movesStraight = False
	movesDiagonal = False
	movesSideways = False
	movesL = False
	onlyMovesOne = False
	
	def __init__(self, color, name, xpos, ypos):
		self.color = color
		self.name = name
		self.xpos = xpos
		self.ypos = ypos

	def pathClear():
		pass	

	def move(self, xpos, ypos):
		if movingCorrectly and pathClear and spaceEmpty:
			self.xpos = xpos
			self.ypos = ypos

	def take(self, xpos, ypos):
		if movingCorrectly and pathClear and spaceOccupied and oppositeColor and notKing:	
				pass
		
	def reportPosition(self):
		position = (self.name, self.xpos, self.ypos)
		return position

class Pawn(Piece):
	movesStraight = True
	canMoveTwo = True
	onlyMovesOne = True
	takesDiagonal = True

	pass


class Rook(Piece):
	movesStraight = True
	movesSideways = True
	pass

class Knight(Piece):
	jumpPieces = True
	movesL = True
	pass

class Bishop(Piece):
	movesDiagonal = True
	pass

class Queen(Piece):
	movesDiagonal = True
	movesSideways = True
	movesStraight = True
	pass

class King(Piece):
	movesDiagonal = True
	movesSideways = True
	movesStraight = True
	onlyMovesOne = True
	pass

class Board:
	occupied = {}

def 
