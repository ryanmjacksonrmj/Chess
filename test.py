for square_on in range(0,64):
	lower= square_on - 7 * (min(7 - (square_on % 8), (square_on // 8)))
	upper= square_on + 7 * (min((square_on % 8), (7 - square_on // 8)))
	# upper= square_on + 9 * ((min(8 - (square_on % 8), 8 - (square_on // 8))) -1)
	# upper = square_on + 9 * (min((square_on % 8), square_on // 8))
	print ("Square " + str(square_on))
	# print ("Lower: " + str(lower))
	print ("Upper: " + str(upper))
