class Piece:
	def __init__(self, is_white, square):
		self.is_white = is_white
		self.square = square
		self.moves_only_one = False
		self.moved_yet = True
		self.possible_moves = set()

class Rook(Piece):
	def __init__(self, is_white, square):
		super().__init__(is_white, square)


a = Piece(True, 25)

b = Rook(True, 15)


print(a.moved_yet)
print(b.moved_yet)