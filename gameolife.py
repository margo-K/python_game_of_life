import numpy as np
from time import sleep

SIZE = 100


def is_alive(i,j,board):
	current_board = board
	cell_alive = current_board[i,j]
	num_alive = alive_neighbors(i,j,current_board)

	if num_alive == 3:
		return True
	else: 
		if cell_alive and num_alive ==2:
			return True
	return False

def update_board(old_board,size=SIZE,alive_checker=is_alive):
	new_array = np.zeros((size,size))
	for j in range(size):
		for i in range(size):
			if alive_checker(i,j,old_board):
				new_array[i,j]=1
	return new_array

def print_to_screen(board_array,size=SIZE,highlight=False):
	representation = ''
	for j in range(size):
		for i in range(size):
			if board_array[i,j]==1:
				representation = representation + "X"
			else:
				representation = representation + "."
		representation = representation + "\n"
	if highlight==True:
		representation = '033[94m'+ representation+'\033[0m'
	print representation

def neighbors(i,j):
	neighbors = []
	count_alive = 0
	for y_offset in [-1,0,1]:
		for x_offset in [-1,0,1]:
			neighbor_x,neighbor_y = i+x_offset,j+y_offset
			if neighbor_x not in range(SIZE) or neighbor_y not in range(SIZE):
				pass
			else:
				neighbors.append((neighbor_x,neighbor_y))
	neighbors.remove((i,j))
	return neighbors

def alive_neighbors(i,j,board):
	neighbors_list = neighbors(i,j)
	alive = [board[element[0],element[1]] for element in neighbors_list]
	return sum(alive)

def random_board(size=SIZE):
	SIZE = size
	return np.random.randint(2,size=(size,size))

if __name__ == '__main__':
	current_board = random_board()
	while True:
		print_to_screen(current_board)
		new_board = update_board(current_board)
		current_board = new_board
		
	