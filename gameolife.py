import numpy as np

def render(array,size,probability):
	representation = ''

	for j in range(size):
		for i in range(size):
			if array[i,j]<=probability:
				representation = representation + "X"
			else:
				representation = representation + "."
		representation = representation + "\n"

	print representation

def random_board(size):
	probability = np.random.random()
	board = np.random.random((size,size))
	print probability, board
	render(board,size,probability)



if __name__ == '__main__':
	random_board(4)
	