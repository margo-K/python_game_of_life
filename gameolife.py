import numpy as np

DEFAULT_PROBABILITY = np.random.random()

def render(board_array,size,alive_check):
	representation = ''

	for j in range(size):
		for i in range(size):
			if alive_check(board_array[i,j]):
				representation = representation + "X"
			else:
				representation = representation + "."
		representation = representation + "\n"

	print representation

def check_prob(cell_value,probability=DEFAULT_PROBABILITY):
	if cell_value <= probability:
		return True
	return False

def check_neighbors(cell_alive,alive_neighbors):
	if alive_neighbors == 3:
		return True
	else: 
		if cell_alive and alive_neighbors ==2:
			return True
	return False

def return_neighbors(i,j):
	neighbors = []
	for y_offset in [-1,0,1]:
		for x_offset in [-1,0,1]:
			neighbors.append((i+x_offset,j+y_offset))
	return neighbors


def random_board(size):
	board = np.random.random((size,size))
	print DEFAULT_PROBABILITY, board
	render(board,size,check_prob)



if __name__ == '__main__':
	random_board(4)
	