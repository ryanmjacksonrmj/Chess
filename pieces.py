from board import *

class Piece:
	def __init__(self, is_white, square):
		self.is_white = is_white
		self.square = square
		self.moved_yet = False
		self.possible_moves = set()

class Pawn(Piece):
	def set_possible_moves(self):
		# Currently doesn't include a check to see if there's an enemy on the diagonal square.
		# No functionality for en passant or promotion.
		if self.is_white == True:
			self.possible_moves.add(self.square + 1)
			self.possible_moves.add(self.square - 7)
			self.possible_moves.add(self.square + 9)
			if self.moved_yet == False:
				self.possible_moves.add(self.square + 2)
		else:
			self.possible_moves.add(self.square -1)
			self.possible_moves.add(self.square + 7)
			self.possible_moves.add(self.square - 9)
			if self.moved_yet == False:
				self.possible_moves.add(self.square - 2)

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