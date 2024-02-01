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
		if is_white == True:
			self.piece_name = "WP" 
		else:
			self.piece_name = "BP"

class Rook(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward", "backward", "left", "right")
		if is_white == True:
			self.piece_name = "WR" 
		else:
			self.piece_name = "BR"
	
class Knight(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		if is_white == True:
			self.piece_name = "WN" 
		else:
			self.piece_name = "BN"

class Bishop(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward_left", "forward_right", "backward_left", "backward_right")
		if is_white == True:
			self.piece_name = "WB" 
		else:
			self.piece_name = "BB"

class Queen(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.movement_type = ("forward", "backward", "left", "right", "forward_left", "forward_right", "backward_left", "backward_right")
		if is_white == True:
			self.piece_name = "WQ" 
		else:
			self.piece_name = "BQ"		

class King(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)
		self.moves_only_one = True
		self.movement_type = ("forward", "backward", "left", "right", "forward_left", "forward_right", "backward_left", "backward_right")
		if is_white == True:
			self.piece_name = "WK" 
		else:
			self.piece_name = "BK"		