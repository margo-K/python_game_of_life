import numpy as np
from time import sleep
import os
import curses
stdscr = curses.initscr()

DEFAULT_SIZE = 100

def random_board(size):
	return np.random.randint(2,size=(size,size))

class Game:
	def __init__(self,size=DEFAULT_SIZE):
		self.board = random_board(size=size)
		self.board_dimension = self.board.shape[0]
		print "The board dimension is {}".format(self.board_dimension)
		self.print_board()

	def update_board(self,alive_condition=None):
		if alive_condition == None:
			alive_condition = self.conway_condition
		new_array = np.zeros((self.board_dimension,self.board_dimension))
		for j in range(self.board_dimension):
			for i in range(self.board_dimension):
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

	def print_board(self,highlight=False): ## could map and join
		stdscr.refresh()
		string_board = ''
		for j in range(self.board_dimension):
			for i in range(self.board_dimension):
				string_board+=self.represent_cell(i,j)
			string_board+="\n"
		print string_board+"\r"

	def represent_cell(self,i,j):
		if self.board[i,j] ==1:
			return "*"
		else:
			return " "

	def neighbors(self,i,j,max_value=None):
		if max_value == None:
			max_value = self.board_dimension
		count_alive = 0
		offsets = [-1,0,1]
		cartesian_product = [(x,y) for x in offsets for y in offsets if not (y==0 and x==0)]
		neighbor_coordinates = [(x+i,y+j) for (x,y) in cartesian_product if x+i<max_value and y+j<max_value]
		return neighbor_coordinates

	def alive_neighbors(self,i,j):
		neighbors_list = self.neighbors(i,j)
		alive = [self.board[element[0],element[1]] for element in neighbors_list]
		return sum(alive)

# class Cell:
# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y
# 	def 

if __name__ == '__main__':
	g = Game()
	while True:
		g.update_board()