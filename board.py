class Board:
	def __init__(self):
		self.squares = {}	
		for key in range (0,64):
			self.squares[key] = Square(key)


class Square:
	def __init__(self, number):
		self.piece = None
		self.number = number
		self.border = set()
		if number in range(0,8):
			self.border.add("left")
		if number in range(7,64,8):
			self.border.add("top")
		if number in range(56,64):
			self.border.add("right")
		if number in range(0,57,8):
			self.border.add("bottom")

		if "left" in self.border:
			self.squares_left = range(0, 0)
		else:
			self.squares_left = range(number - 8, (number % 8) -1, -8)
		if "right" in self.border:
			self.squares_right = range(0, 0)
		else:
			self.squares_right = range(number +8, number % 8 + 57, 8)

		if "top" in self.border:
			self.squares_forward = range(0, 0)
		else:
			self.squares_forward = range(number + 1, self.number + 8 - self.number % 8)
		if "bottom" in self.border:
			self.squares_backward = range (0,0)
		else:
			self.squares_backward = range(number -1, number - number % 8 -1, -1)
		
		if "top" in self.border or "left" in self.border:
			self.squares_diagonal_forward_left = range (0, 0)
		else:
			self.squares_diagonal_forward_left = range(number - 7, number - 7 * (min(7 - (number % 8), (number // 8))) -1, -7)

		if "bottom" in self.border or "right" in self.border:
			self.squares_diagonal_backward_right = range (0,0)
		else:
			self.squares_diagonal_backward_right = range(number + 7, number + 7 * (min((number % 8), (7 - number // 8))) +1, 7)

		if "top" in self.border or "right" in self.border:
			self.squares_diagonal_forward_right = range(0,0)
		else:
			self.squares_diagonal_forward_right = range(number + 9, number + 9 * ((min(8 - (number % 8), 8 - (number // 8))) -1) + 1, 9)
		
		if "bottom" in self.border or "left" in self.border:
			self.squares_diagonal_backward_left = range(0,0)
		else:	
			self.squares_diagonal_backward_left = range(number -9, self.number - 9 * (min((self.number % 8), self.number // 8)) -1, -9)
	
	def nearest_piece(self,):