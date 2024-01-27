from board import *

class Piece:
	def __init__(self, is_white, square):
		self.is_white = is_white
		self.square = square
		self.moves_only_one = False
		self.moved_yet = False
		self.movement_type = set()
		self.possible_moves = set()

class Pawn(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("foward", "backward", "forward_left", "forward_right", "backward_left", "backward_right")
	
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
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("foward", "backward", "left", "right")
	
class Knight(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("knight_move")

class Bishop(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward_left", "forward_right", "backward_left", "backward_right")

class Queen(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("foward", "backward", "left", "right", "forward_left", "forward_right", "backward_left", "backward_right")

class King(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.moves_only_one = True
		self.movement_type = ("foward", "backward", "left", "right", "forward_left", "forward_right", "backward_left", "backward_right")