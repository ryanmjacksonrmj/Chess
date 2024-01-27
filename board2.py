class Board:
	def __init__(self):
		self.squares = {}	
		for key in range (0,64):
			self.squares[key] = Square(key)

class Square:
	def __init__(self, number):
		self.piece = None
		self.number = number
		self.nearest_pieces = {}
		self.white_moves = {}
		self.black_moves = {}
		self.border = set()
		if number in range(0,8):
			self.border.add("left")
		if number in range(7,64,8):
			self.border.add("top")
		if number in range(56,64):
			self.border.add("right")
		if number in range(0,57,8):
			self.border.add("bottom")
		# self.neighbors holds a dictionary of squares a piece could travel to from the current square given a direction (e.g. forward) assuming there are no other pieces in the way
		self.neighbors = {}
		
		if "left" in self.border:
			self.neighbors['left'] = range(0)
		else:
			self.neighbors['left'] = range(number - 8, (number % 8) -1, -8)
		if "right" in self.border:
			self.neighbors['right'] = range(0)
		else:
			self.neighbors['right'] = range(number +8, number % 8 + 57, 8)

		if "top" in self.border:
			self.neighbors['forward'] = range(0)
		else:
			self.neighbors['forward'] = range(number + 1, self.number + 8 - self.number % 8)
		if "bottom" in self.border:
			self.neighbors['backward'] = range(0)
		else:
			self.neighbors['backward'] = range(number -1, number - number % 8 -1, -1)
	
		if "top" in self.border or "left" in self.border:
			self.neighbors['forward_left'] = range(0)
		else:
			self.neighbors['forward_left'] = range(number - 7, number - 7 * (min(7 - (number % 8), (number // 8))) -1, -7)

		if "bottom" in self.border or "right" in self.border:
			self.neighbors['backward_right'] = range(0)
		else:
			self.neighbors['backward_right'] = range(number + 7, number + 7 * (min((number % 8), (7 - number // 8))) +1, 7)

		if "top" in self.border or "right" in self.border:
			self.neighbors['forward_right'] = range(0)
		else:
			self.neighbors['forward_right'] = range(number + 9, number + 9 * ((min(8 - (number % 8), 8 - (number // 8))) -1) + 1, 9)
		
		if "bottom" in self.border or "left" in self.border:
			self.neighbors['backward_left'] = range(0)
		else:	
			self.neighbors['backward_left'] = range(number -9, self.number - 9 * (min((self.number % 8), self.number // 8)) -1, -9)
	
	#This traverses the list of spaces in self.neighbors and determines what the closest space is to the square in each direction with a piece on it
	def get_nearest_pieces(self, board):
		is_white = self.piece.is_white
		self.white_moves = {}
		self.black_moves = {}
		self.moves = {}
		#going through the directions you can travel
		for i in self.neighbors:
			#going through the squares in that direction
			for j in self.neighbors[i]:
				#if it comes to a space that has a piece
				if board.squares[j].piece != None:
					# if the piece on that square is white
					if board.squares[j].piece.is_white == is_white:
						#Add an entry to the self.white_moves dictionary with key of direction of movement and value of 
						self.moves[i] = range(self.neighbors[i].start, board.squares[j].number, self.neighbors[i].step)
					# if the piece on that square is black		
					else:
						if self.neighbors[i].step < 0:
							self.moves[i] = range(self.neighbors[i].start, board.squares[j].number -1, self.neighbors[i].step)
						else:
							self.moves[i] = range(self.neighbors[i].start, board.squares[j].number +1, self.neighbors[i].step)
					break
		for i in self.neighbors:
			if i not in self.black_moves :
				if not self.neighbors[i]:
					self.black_moves[i] = None
				else:
					self.black_moves[i] = self.neighbors[i][-1]
			if i not in self.white_moves:
				if not self.neighbors[i]:
					self.white_moves[i] = None
				else:
					self.white_moves[i] = self.neighbors[i][-1]

	def knight_move(self, board):
		distance = (10, 17, 15, 6, -6, -10, -17, -15)
		moves = set()
		self.knight_black_moves = set()
		self.knight_white_moves = set()
		for entity in distance:
			new_square = self.number + entity
			if new_square >= 0 and new_square <= 63 and (abs((self.number % 8) - ((new_square) % 8)) <= 2):
				moves.add(new_square)
		for move in moves:
			if board.squares[move].piece != None:
				if board.squares[move].piece.is_white == True:
					self.knight_black_moves.add(move)
				else:
					self.knight_white_moves.add(move)
			else:
				self.knight_black_moves.add(move)
				self.knight_white_moves.add(move)
	
	def get_moves(self):
		if self.piece == None:
			return None
		else:
			piece = self.piece
		movement_type = piece.movement_type
