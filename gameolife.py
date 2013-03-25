import numpy as np

DEFAULT_PROBABILITY = np.random.random()

def render(array,size,alive_check):
	representation = ''

	for j in range(size):
		for i in range(size):
			if alive_check(array[i,j]):
				representation = representation + "X"
			else:
				representation = representation + "."
		representation = representation + "\n"

	print representation

def check_prob(cell_value,probability=DEFAULT_PROBABILITY):
	if cell_value <= probability:
		return True
	return False

def random_board(size):
	board = np.random.random((size,size))
	print DEFAULT_PROBABILITY, board
	render(board,size,check_prob)

def will_live(cell_alive,alive_neighbors):
	if alive_neighbors == 3:
		return True
	else: 
		if cell_alive and alive_neighbors ==2:
			return True
	return False


if __name__ == '__main__':
	random_board(4)
	