def move_type(starting_space, ending_space):
	change_in_x = abs(starting_space[0] - ending_space[0])
	change_in_y = abs(starting_space[1] - ending_space[1])
	if starting_space == ending_space:
		return 0 # The player didn't move
	elif starting_space[0] == ending_space[0]:
		return 1 # Vertical movement
	elif starting_space[1] == ending_space[1]:
		return 2 # Horizontal movement
	elif change_in_x == change_in_y:
		return 3 # Diagonal movement
	elif (change_in_x == 1 and change_in_y == 2) or (change_in_x == 2 and change_in_y == 1):
		return 4 # L-shaped (i.e knight) move
	else:
		return -1 # Invalid move