import numpy as np
from time import sleep

DEFAULT_SIZE = 100

def random_board(size=DEFAULT_SIZE):
	return np.random.randint(2,size=(size,size))


class Game:
	def __init__(self,size=DEFAULT_SIZE):
		self.size = size
		self.board = random_board()
		self.print_board()

	def update_board(self,alive_condition=None):
		if alive_condition == None:
			alive_condition = self.conway_condition
		new_array = np.zeros((self.size,self.size))
		for j in range(self.size):
			for i in range(self.size):
				if alive_condition(i,j):
					new_array[i,j]=1
		self.board = new_array
		self.print_board()

	def conway_condition(self,i,j): ## should perhaps be outside of the game class
		current_board = self.board
		if self.alive_neighbors(i,j) == 3:
			return True
		else: 
			if current_board[i,j]==1 and self.alive_neighbors(i,j) ==2: ## aka current_board[i,j]+num_alive == 3
				return True
		return False 

	def print_board(self,size=DEFAULT_SIZE,highlight=False): ## could map and join
		string_board = ''
		for j in range(size):
			for i in range(size):
				string_board+=self.represent_cell(i,j)
			string_board+="\n"
		# if highlight==True:
		# 	representation = '033[94m'+ representation+'\033[0m'
		print string_board

	def represent_cell(self,i,j):
		if self.board[i,j] ==1:
			return "*"
		else:
			return " "

	def neighbors(self,i,j,max_value=None):
		if max_value == None:
			max_value = self.size
		neighbors_list = []
		count_alive = 0
		for y_offset in [-1,0,1]:
			for x_offset in [-1,0,1]:
				neighbor_x,neighbor_y = i+x_offset,j+y_offset
				if neighbor_x not in range(max_value) or neighbor_y not in range(max_value):
					pass
				else:
					neighbors_list.append((neighbor_x,neighbor_y))
		neighbors_list.remove((i,j))
		return neighbors_list

	def alive_neighbors(self,i,j):
		neighbors_list = self.neighbors(i,j)
		alive = [self.board[element[0],element[1]] for element in neighbors_list]
		return sum(alive)


if __name__ == '__main__':
	g = Game()
	while True:
		g.update_board()