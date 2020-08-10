import pygame
from a_star_algorithm import a_star 
from gridSquare_class import gridSquare 

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			grid_square = gridSquare(i, j, gap, rows)
			grid[i].append(grid_square)

	return grid


def draw_grid(win, rows, width):
	GREY = (128, 128, 128)
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	WHITE = (255,255,255)
	win.fill(WHITE)

	for row in grid:
		for grid_square in row:
			pygame.draw.rect(win, *grid_square.get_draw_components())

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col


def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				grid_square = grid[row][col]
				if not start and grid_square != end:
					start = grid_square
					start.make_start()

				elif not end and grid_square != start:
					end = grid_square
					end.make_end()

				elif grid_square != end and grid_square != start:
					grid_square.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				grid_square = grid[row][col]
				grid_square.reset()
				if grid_square == start:
					start = None
				elif grid_square == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for grid_square in row:
							grid_square.update_neighbors(grid)

					success = a_star(lambda: draw(win, grid, ROWS, width), grid, start, end)
					if success is None:
						run = False

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

main(WIN, WIDTH)