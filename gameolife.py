import numpy as np
import unittest

DEFAULT_SIZE = 100

offsets = [-1,0,1]
delta_coordinates = [(x,y) for x in offsets for y in offsets if not (y==0 and x==0)] # list of offset coordinates (dx,dy)

def random_board(size):
	return np.random.randint(2,size=(size,size))

def blinker_board():
	return np.array([(0,0,0),(1,1,1),(0,0,0)])

class Game:
	def __init__(self,board):
		self.board = board #an array of 0,1
		self.board_dimension = self.board.shape[0] #all boards are currently square, so shape[0]==shape[1]
		print "The board dimension is {}".format(self.board_dimension)
		self.print_board()

	@classmethod
	def random(cls,size=DEFAULT_SIZE):
		board=random_board(size)
		return cls(board)

	def __eq__(self,other):
		if isinstance(other,self.__class__):
			return (self.board==other.board).all()
		else:
			return False

	def update_board(self,alive_condition=None):
		if alive_condition == None:
			alive_condition = self.conway_condition
		new_array = np.zeros((self.board_dimension,self.board_dimension))
		for j in range(self.board_dimension):
			for i in range(self.board_dimension):
				if alive_condition(i,j):
					new_array[i,j]=1
		self.board = new_array
		return self

	def conway_condition(self,i,j):
		current_board = self.board
		if self.alive_neighbors(i,j) == 3:
			return True
		else: 
			if current_board[i,j]==1 and self.alive_neighbors(i,j) ==2:
				return True
		return False 

	def __str__(self):
		string_board = ''
		for j in range(self.board_dimension):
			for i in range(self.board_dimension):
				string_board+=self.represent_cell(i,j)
			string_board+="\n"
		return string_board+"\r"

	def print_board(self,highlight=False): ## could map and join
		print self
	
	def represent_cell(self,i,j):
		if self.board[i,j] ==1:
			return "X"
		else:
			return "."

	def neighbors(self,i,j):
		max_value = self.board_dimension
		neighbor_coordinates = [(x+i,y+j) for (x,y) in delta_coordinates if (0<=(x+i)<max_value) and (0<=(y+j)<max_value)]
		return neighbor_coordinates

	def alive_neighbors(self,i,j):
		neighbors_list = self.neighbors(i,j)
		neighbor_values = [self.board[element[0],element[1]] for element in neighbors_list]
		return sum(neighbor_values)


class GameTest(unittest.TestCase):
	def test_blinker(self):
		board1 = blinker_board()
		board2 = blinker_board()
		g = Game(board1) 
		g2 = Game(board2)

		g2.update_board().update_board()

		self.assertEquals(g,g2)

	def test_NW_corner(self):
		g = Game.random(3)
		i,j = (0,0)
		expected_neighbors = set([(0,1),(1,0),(1,1)])
		self.assertEquals(set(g.neighbors(i,j)),expected_neighbors)


	def test_NE_corner(self):
		g = Game.random(3)
		i,j = (0,2)
		expected_neighbors = set([(0,1),(1,2),(1,1)])
		self.assertEquals(set(g.neighbors(i,j)),expected_neighbors)
		


	def test_SE_corner(self):
		g = Game.random(3)
		i,j = (2,0)
		expected_neighbors = set([(1,1),(1,0),(2,1)])
		self.assertEquals(set(g.neighbors(i,j)),expected_neighbors)
		

	def test_SW_corner(self):
		g = Game.random(3)
		i,j = (2,2)
		expected_neighbors = set([(2,1),(1,2),(1,1)])
		self.assertEquals(set(g.neighbors(i,j)),expected_neighbors)
		

if __name__ == '__main__':
	g = Game.random()
	while True:
		g.update_board()
		print g