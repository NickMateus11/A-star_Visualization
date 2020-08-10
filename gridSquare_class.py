
class gridSquare:

	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 255, 0)
	YELLOW = (255, 255, 0)
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	PURPLE = (128, 0, 128)
	ORANGE = (255, 165 ,0)
	GREY = (128, 128, 128)
	TURQUOISE = (64, 224, 208)

	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = gridSquare.WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == gridSquare.RED

	def is_open(self):
		return self.color == gridSquare.GREEN

	def is_barrier(self):
		return self.color == gridSquare.BLACK

	def is_start(self):
		return self.color == gridSquare.ORANGE

	def is_end(self):
		return self.color == gridSquare.TURQUOISE

	def reset(self):
		self.color = gridSquare.WHITE

	def make_start(self):
		self.color = gridSquare.ORANGE

	def make_closed(self):
		self.color = gridSquare.RED

	def make_open(self):
		self.color = gridSquare.GREEN

	def make_barrier(self):
		self.color = gridSquare.BLACK

	def make_end(self):
		self.color = gridSquare.TURQUOISE

	def make_path(self):
		self.color = gridSquare.PURPLE

	def get_draw_components(self):
		return (self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False