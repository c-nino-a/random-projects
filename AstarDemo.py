import time
import numpy as np
import sys
import pygame
import math


max_possible_value = sys.maxsize
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.init()
pygame.display.set_caption("A* Path Finding Algorithm")
HOW=0
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
BLACK = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.width = width
		self.total_rows = total_rows


	def get_name(self):
		return self.name

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
		
	def __lt__(self, other):
		return False


def astar_search(graph, start, goal):
    path = []
    explored_nodes = list()
 
    if start == goal:
        return path, explored_nodes
    path.append(start)
    path_cost = get_manhattan_heuristic(start, goal)
    
   
    frontier = [(path_cost, path)]

    while len(frontier) > 0:

        path_cost_till_now, path_till_now = pop_frontier(frontier)
        current_node = path_till_now[-1]
        
        path_cost_till_now = path_cost_till_now - get_manhattan_heuristic(current_node, goal)
        explored_nodes.append(current_node)

        if current_node == goal:
            return path_till_now, explored_nodes
        neighbours = graph[current_node]
        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int.sort(reverse=False)
        neighbours_list_str = [str(n) for n in neighbours_list_int]
        for neighbour in neighbours_list_str:
            path_to_neighbour = path_till_now.copy()
            path_to_neighbour.append(neighbour)

            extra_cost = 1
            neighbour_cost = extra_cost + path_cost_till_now + get_manhattan_heuristic(neighbour, goal)
            new_element = (neighbour_cost, path_to_neighbour)
            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(neighbour, frontier)
            if (neighbour not in explored_nodes) and not is_there:
                frontier.append(new_element)

            elif is_there:
                if neighbour_old_cost > neighbour_cost:
                    frontier.pop(indexx)
                    frontier.append(new_element)
    
    return None, None

def pop_frontier(frontier):
    if len(frontier) == 0:
        return None

    min = max_possible_value
    max_values = []
    for key, path in frontier:


        if key == min:
            max_values.append(path)
        elif key < min:

            min = key
            max_values.clear()
            max_values.append(path)
    max_values = sorted(max_values, key=lambda x: x[-1])

    desired_value = max_values[0]

    frontier.remove((min, max_values[0]))

    return min, desired_value

def get_frontier_params_new(node, frontier):
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path
    return False, None, None, None

def get_manhattan_heuristic(node, goal):
    i, j = divmod(int(node), 8  )
    i_goal, j_goal = divmod(int(goal), 8)
    i_delta = abs(i - i_goal)
    j_delta = abs(j - j_goal)

    manhattan_dist = i_delta + j_delta
    return manhattan_dist

graph_neighbours = {}

def generate_graph():
    add_neighbours('0', ['8', '1'])
    add_neighbours('1', ['0', '2'])
    add_neighbours('2', ['10', '1'])
    add_neighbours('3', ['11', '4'])
    add_neighbours('4', ['3', '5'])
    add_neighbours('5', ['4', '6'])
    add_neighbours('6', ['5'])
    add_neighbours('7', ['15'])
    add_neighbours('8', ['0', '16', '9'])
    add_neighbours('9', ['8'])
    add_neighbours('10', ['2', '18'])
    add_neighbours('11', ['3', '19'])
    add_neighbours('12', ['13'])
    add_neighbours('13', ['12', '14', '21'])
    add_neighbours(14, [13, 15])
    add_neighbours(15, [7, 14, 23])
    add_neighbours(16, [8, 17, 24])
    add_neighbours(17, [16])
    add_neighbours(18, [10, 19])
    add_neighbours(19, [11, 20, 18])
    add_neighbours(20, [19, 28])
    add_neighbours(21, [13, 22])
    add_neighbours(22, [21])
    add_neighbours(23, [15, 31])
    add_neighbours(24, [16, 25])
    add_neighbours(25, [24, 26])
    add_neighbours(26, [25, 27])
    add_neighbours(27, [26, 35])
    add_neighbours(28, [20, 29])
    add_neighbours(29, [28, 30])
    add_neighbours(30, [29, 31])
    add_neighbours(31, [30, 23])
    add_neighbours(32, [40, 33])
    add_neighbours(33, [32, 34])
    add_neighbours(34, [33, 35])
    add_neighbours(35, [27, 34, 36])
    add_neighbours(36, [35, 37])
    add_neighbours(37, [36])
    add_neighbours(38, [46, 39])
    add_neighbours(39, [38, 47])
    add_neighbours(40, [32, 48])
    add_neighbours(41, [49, 42])
    add_neighbours(42, [41, 50, 43])
    add_neighbours(43, [42, 51, 44])
    add_neighbours(44, [43, 45])
    add_neighbours(45, [44, 46, 53])
    add_neighbours(46, [45, 38])
    add_neighbours(47, [39, 55])
    add_neighbours(48, [40, 56])
    add_neighbours(49, [41, 50])
    add_neighbours(50, [49, 42])
    add_neighbours(51, [43, 59])
    add_neighbours(52, [53])
    add_neighbours(53, [61, 52, 45])
    add_neighbours(54, [62])
    add_neighbours(55, [47, 63])
    add_neighbours(56, [48, 57])
    add_neighbours(57, [56, 58])
    add_neighbours(58, [57, 59])
    add_neighbours(59, [58, 51, 60])
    add_neighbours(60, [59])
    add_neighbours(61, [53])
    add_neighbours(62, [54, 63])
    add_neighbours(63, [55, 62])
    return graph_neighbours

def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def make_grid(rows, width):
	grid = []
	gap = width // rows
	k=0
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)
			k+=1

	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	pygame.draw.line(win, BLACK, (4 * gap, 0*gap), (4 * gap, 3*gap))
	pygame.draw.line(win, BLACK, (3 * gap, 1*gap), (3 * gap, 4*gap))
	pygame.draw.line(win, BLACK, (4 * gap, 4*gap), (4 * gap, width))
	pygame.draw.line(win, BLACK, (5 * gap, 1*gap), (5 * gap, 6*gap))
	pygame.draw.line(win, BLACK, (1 * gap, 1*gap), (1 * gap, 2*gap))
	pygame.draw.line(win, BLACK, (2 * gap, 1*gap), (2 * gap, 2*gap))
	pygame.draw.line(win, BLACK, (1 * gap, 4*gap), (1 * gap, 7*gap))
	pygame.draw.line(win, BLACK, (2 * gap, 4*gap), (2 * gap, 5*gap))
	pygame.draw.line(win, BLACK, (2 * gap, 6*gap), (2 * gap, 6*gap))
	pygame.draw.line(win, BLACK, (3 * gap, 5*gap), (3 * gap, 7*gap))
	pygame.draw.line(win, BLACK, (7 * gap, 1*gap), (7 * gap, 3*gap))
	pygame.draw.line(win, BLACK, (5 * gap, 4*gap), (5 * gap, 5*gap))
	pygame.draw.line(win, BLACK, (7 * gap, 4*gap), (7 * gap, 5*gap))
	pygame.draw.line(win, BLACK, (2 * gap, 6*gap), (2 * gap, 7*gap))
	pygame.draw.line(win, BLACK, (6 * gap, 6*gap), (6 * gap, 7*gap))
	pygame.draw.line(win, BLACK, (6 * gap, 4*gap), (6 * gap, 5*gap))

	pygame.draw.line(win, BLACK, (0*gap, 3 * gap), (2*gap, 3 * gap))
	pygame.draw.line(win, BLACK, (0*gap, 7 * gap), (1*gap, 7 * gap))
	pygame.draw.line(win, BLACK, (1*gap, 2 * gap), (2*gap, 2 * gap))
	pygame.draw.line(win, BLACK, (1*gap, 4 * gap), (2*gap, 4 * gap))
	pygame.draw.line(win, BLACK, (2*gap, 2 * gap), (3*gap, 2 * gap))
	pygame.draw.line(win, BLACK, (2*gap, 5 * gap), (3*gap, 5 * gap))
	pygame.draw.line(win, BLACK, (2*gap, 7 * gap), (3*gap, 7 * gap))
	pygame.draw.line(win, BLACK, (3*gap, 4 * gap), (4*gap, 4 * gap))
	pygame.draw.line(win, BLACK, (4*gap, 6 * gap), (5*gap, 6 * gap))
	pygame.draw.line(win, BLACK, (5*gap, 1 * gap), (7*gap, 1 * gap))
	pygame.draw.line(win, BLACK, (5*gap, 7 * gap), (7*gap, 7 * gap))
	pygame.draw.line(win, BLACK, (5*gap, 7 * gap), (7*gap, 7 * gap))
	pygame.draw.line(win, BLACK, (6*gap, 3 * gap), (7*gap, 3 * gap))
	pygame.draw.line(win, BLACK, (6*gap, 4 * gap), (7*gap, 4 * gap))
	pygame.draw.line(win, BLACK, (6*gap, 6 * gap), (8*gap, 6 * gap))
	pygame.draw.line(win, BLACK, (6*gap, 7 * gap), (7*gap, 7 * gap))
	pygame.draw.line(win, BLACK, (7*gap, 5 * gap), (8*gap, 5 * gap))

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	weights(rows,width)	

	draw_grid(win, rows, width)
	
	pygame.display.update()

def weights(rows,width):
	myfont = pygame.font.SysFont('arial', 20)
	gap = width // rows / 2
	j=0
	for i in range(8):
		for k in range(8):
			text=myfont.render(str(j),False,(0,0,0))
			WIN.blit(text,((i*2+1)*gap,(k*2+1)*gap))
			j+=1

def main(win, width):
	ROWS = 8
	grid = make_grid(ROWS, width)

	start = grid[0][0]

	end = grid[7][5]

	start.make_start()
	end.make_end()

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					path_astar, explored_astar = astar_search(graph_neighbours, '0', '61')
					print(explored_astar)
					for i in explored_astar:
					    if(i!=61):
					        grid[int(i)//8][int(i)%8].make_closed()
					        time.sleep(.1)
					        draw(win,grid,ROWS,width)
					path_astar.reverse()
					for i in path_astar:
						grid[int(i)//8][int(i)%8].make_path()
						time.sleep(.02)
						draw(win,grid,ROWS,width)

	pygame.quit()


if __name__ == '__main__':
    graph_neighbours = generate_graph()
    main(WIN, WIDTH)

