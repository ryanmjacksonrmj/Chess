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

class Black_Pawn(Pawn):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("backward", "backward_left", "backward_right")

class Black_Pawn(Pawn):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("foward", "forward_left", "forward_right")

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