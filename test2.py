for i in range(0,64):
	upper= i + 9 * (min(8 - (i % 8), 8 - (i // 8)))
	a = i % 8
	b = i // 8
	# print("Square: " + str(i) + " " + str(lower) + " " + str(upper))
	print("Square " + str(i) + " A= " + str(a) + " B= " + str(b) + " Upper= " + str(upper))