from Node import *
from Grid import *

"""BONUS: Get user input for 
goal and current state"""

def main():
	grid = readGrid("grid.txt")
	for i in grid:
		print(i)
	start = [5,1]
	goal = [2,4]
	path = uninformedSearch(grid, start, goal)
	print("\nPATH")
	for i in path:
		print(i)

	outputGrid(grid, start, goal, path)

def uninformedSearch(grid, start, goal, search="bfs"):
	# Assume start and goal are just locations
	closed = []
	current = None
	starting_node = Node(start, None)
	frontier = []
	frontier.append(starting_node)
	while True:
		current = frontier.pop(0)
		# ---DEBUG---
		print("Current Value: " + str(current.value))
		# -----------
		for node in expandNode(current, grid):
			if not inList(node, frontier):
				frontier.append(node)
		# ---DEBUG---
		print("----FRONTIER----")
		for el in frontier:
			print(el.value)
		print("----------------")
		# -----------

		if not inList(current, closed):
			closed.append(current)
		# ---DEBUG---
		print("####CLOSED####")
		for el in closed:
			print(el.value)
		print("##############")
		# -----------

		if(current.value == goal):
			print("GOAL REACHED")
			path = setPath(current)
			return path
		if(len(frontier) == 0):
			# return empty list if unsuccessful
			print("FAILURE")
			return None
		

def getNeighbors(location, grid):
	neighbors = []
	
	# CHECK UP
	if(location[0]-1 > -1 and grid[location[0]-1][location[1]] != 1):
		neighbors.append([location[0]-1, location[1]])

	# CHECK RIGHT
	if(location[1]+1 < len(grid[location[0]]) and grid[location[0]][location[1]+1] != 1):
		neighbors.append([location[0], location[1]+1])

	# CHECK DOWN
	if(location[0]+1 < len(grid) and grid[location[0]+1][location[1]] != 1):
		neighbors.append([location[0]+1, location[1]])

	# CHECK LEFT
	if(location[1]-1 > -1 and grid[location[0]][location[1]-1] != 1):
		neighbors.append([location[0], location[1]-1])

	return neighbors

def expandNode(node, grid):
	nodes = []
	neighbors = getNeighbors(node.value, grid)
	for value in neighbors:
		nodes.append(Node(value, node))
	return nodes

def setPath(current):
	path = [current.value]
	while(current.parent != None):
		path.append(current.parent.value)
		current = current.parent
	return path

def inList(node, nodes):
	for n in nodes:
		if(n.value[0] == node.value[0] 
			and n.value[1] == node.value[1]):
			return True
	return False


if __name__ == "__main__":
	main();