class Piece:
	def __init__(self, is_white, square):
		self.is_white = is_white
		self.square = square
		self.moved_yet = False
		self.movement_type = set()
		self.possible_moves = set()

class Pawn(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward", "backward", "forward_left", "forward_right", "backward_left", "backward_right")

class Rook(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward", "backward", "left", "right")
	
class Knight(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)

class Bishop(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward_left", "forward_right", "backward_left", "backward_right")

class Queen(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward", "backward", "left", "right", "forward_left", "forward_right", "backward_left", "backward_right")

class King(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.moves_only_one = True
		self.movement_type = ("forward", "backward", "left", "right", "forward_left", "forward_right", "backward_left", "backward_right")