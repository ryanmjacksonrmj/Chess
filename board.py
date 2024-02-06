from pieces import *
from ascii import *

class Board:
	def __init__(self):
		self.board = self
		self.squares = {}
		self.map = []
		self.ascii = Ascii()
		self.white_to_move = True
		self.algebraic_squares = set()	
		for key in range (0,64):
			self.squares[key] = Square(key)
		columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		rows = range(8, 0,-1)
		for column in columns:
			for row in rows:
				algebraic_square = column + str(row)
				self.algebraic_squares.add(algebraic_square)

	def get_map(self):
		self.map = []
		for square in self.squares:
			piece = self.squares[square].piece
			if piece == None:
				self.map.append("  ")
			else:
				self.map.append(piece.piece_name)

	def new_game(self):
		piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
		is_white = True
		for square in range (1,58,8):
			self.squares[square].piece = Pawn(is_white, square)
		piece_iterator = iter(piece_order)
		for square in range (0,57,8):
				self.squares[square].piece = next(piece_iterator)(is_white, square)
		is_white = False
		for square in range (6,63,8):
			self.squares[square].piece = Pawn(is_white, square)
		piece_iterator = iter(piece_order)
		for square in range (7,64,8):
				self.squares[square].piece = next(piece_iterator)(is_white, square)
	
	def update_moves(self):
		for square in self.squares:
			self.squares[square].get_piece_moves(self.board)
	
class Square:
	def __init__(self, number):
		self.piece = None
		self.number = number
		self.algebraic = None
		self.nearest_pieces = {}
		self.piece_moves = set()
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
		columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		rows = ['8', '7', '6', '5', '4', '3', '2', '1']
		column_index = number // 8
		row_index = number % 8
		self.algebraic = columns[column_index] + rows[row_index]
		
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
	
	#This traverses the list of spaces in self.neighbors and determines what the closest space is to the square in each direction with a piece on it. Then it sets a dictionary ("moves") that says how far a piece can travel given that piece

	def get_moves(self, board):
		self.moves = {}
		if self.piece is None:
			return
		is_white = self.piece.is_white
		#going through the directions you can travel
		for i in self.neighbors:
			#going through the squares in that direction
			for j in self.neighbors[i]:
				#if it comes to a space that has a piece
				if board.squares[j].piece != None:
					# if the piece on that square is the same color, set the range so that it is not included in possible moves
					if board.squares[j].piece.is_white == is_white:
						#Add an entry to the self.moves dictionary with key of direction of movement and value of 
						self.moves[i] = range(self.neighbors[i].start, board.squares[j].number, self.neighbors[i].step)
					# if the piece on that square is opposite color set the range so that it is included in possible moves.
					else:
						if self.neighbors[i].step < 0:
							self.moves[i] = range(self.neighbors[i].start, board.squares[j].number -1, self.neighbors[i].step)
						else:
							self.moves[i] = range(self.neighbors[i].start, board.squares[j].number +1, self.neighbors[i].step)
					break
			# if there are no pieces in a particular direction then all the spaces in that direction 	
			if i not in self.moves:
				self.moves[i] = self.neighbors[i]

	def get_knight_moves(self, board):
		distance = (10, 17, 15, 6, -6, -10, -17, -15)
		moves = set()
		knight_moves = set()
		for entity in distance:
			new_square = self.number + entity
			if new_square >= 0 and new_square <= 63 and (abs((self.number % 8) - ((new_square) % 8)) <= 2):
				moves.add(new_square)
		for move in moves:
			if board.squares[move].piece != None:
				if board.squares[move].piece.is_white != self.piece.is_white:
					self.knight_moves.add(move)
		return knight_moves	
	
	def get_pawn_moves(self, board):
		piece = self.piece
		is_white = piece.is_white
		pawn_moves = set()
		distance = {-7, 9, 1}
		color_determining_multiplier = 1 if is_white else -1
		can_move_two = board.squares[self.number + (1 * color_determining_multiplier)].piece == None
		if piece.moved_yet == False and can_move_two == True:
			distance.add(2)
		for square in distance:
			on_board = False
			test_square = self.number + (square * color_determining_multiplier)
			if test_square >= 0 and test_square <= 63:
				on_board = True
				test_piece = board.squares[test_square].piece
			else:
				on_board = False
			if square > 0 and square <= 2 and on_board == True and test_piece == None:
				pawn_moves.add(test_square)
			elif on_board == True and test_piece == True and piece.color != test_piece.color and square < -2:
				pawn_moves.add(test_square)
			elif on_board == True and test_piece == True and piece.color != test_piece.color and square > 2:
				pawn_moves.add(test_square)
		return pawn_moves

	def get_piece_moves(self, board):
		# This function returns a set with the squares of legal moves in it. To check if a move is valid when the pieces is moved all the program needs to check (when this is fully implemented) is whether or not the destination square of the piece is in this set.
		self.get_moves(board)
		self.piece_moves = set()
		if self.piece == None:
			return
		else:
			piece = self.piece
		movement_type = piece.movement_type
		if type(piece) == Knight:
			self.piece_moves = self.get_knight_moves(board)
		elif type(piece) == King:
			for direction in movement_type:
				#My goal here is to get one square from each movement direction to add to the set. No support here for castling yet. I think not being able to move into check and those sorts of rules will eventually take care of themselves with the other things I need to support check and so don't need to be added here.
				for square in self.moves[direction]:
					self.piece_moves.add(square)
					break
		elif type(piece) == Pawn:
			self.piece_moves = self.get_pawn_moves(board)
		else:
			for direction in movement_type:
				for square in self.moves[direction]:
					self.piece_moves.add(square)


		