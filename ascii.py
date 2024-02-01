class Ascii():

	def __init__(self):
		pass

	def draw_square(self, piece):
		space = "| " + piece + " "
		return space

	def draw_row(self, row_marker, pieces):
		bottom_half = "|\n    " + "|____" * 8 + "|"
		row = " " + row_marker + "  "
		for piece in pieces:
			row += (self.draw_square(piece))
		row += bottom_half
		print(row)

	def draw_board(self, board):
		board.get_map()
		top_row = "     " + "_" * 39
		map = board.map
		row_markers = ["1", "2", "3", "4", "5", "6", "7", "8"]
		column_header = "   " + "   a  " + "  b  " + "  c  " + "  d  " + "  e  " + "  f  " + "  g  " + "  h  "
		row_marker_iterator = iter(row_markers)
		print(top_row)
		for row in range (7,-1,-1):
			pieces = []
			for square in range(row, 64, 8):
				pieces.append(map[square])
			self.draw_row(next(row_marker_iterator), pieces)
		print(column_header, "\n\n")