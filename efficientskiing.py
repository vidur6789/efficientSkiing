import numpy as np
from collections import namedtuple
from enum import Enum



size=5
map = np.random.randint(2*size, size=(size,size))
# initialize distance matrix with -1. Alternatively use np.NaN
distance = np.ones((size, size), dtype=np.int16)
distance = np.negative(distance)
for (i in range(size)):
	for(j in range(size)):
		#TODO ignore non-starters
		start = Position(i, j)
		max_distance=0		
		ski_distance = distance_search(start, max_distance, map, distance)
		max_distance = ski_distance if ski_distance > max_distance else max_distance # TODO tie breaker
		
# returns max ski distance from given starting point		
def distance_search(start, max_distance, map, distance):
	search_stack = next_moves(start, map)
	traversed = 0
	while search_stack:
		# peek
		position = search_stack[-1].to 
		traversed += 1
		# return if already calculated
		if distance[position.xpos][position.ypos] != -1:
			return distance[position.xpos][position.ypos]
		# return -1 if no sense in searching
		if traversed + map[position.xpos][position.ypos] < max_distance:
			return -1
		moves = next_moves(position, map)
		if moves:
			search_stack.extend(moves)
		else:
			distance[position.xpos][position.ypos] = 0
			reverse_distance=1
			while search_stack:
				node = search_stack.pop()
				distance[node.from.xpos][node.from.ypos] = reverse_distance
				reverse_distance+=1
				if not search_stack or node.from == search_stack[-1].from:
					break
				
			traversed-=reverse_distance
	return distance[start.xpos][start.ypos]
		
# return list of moves
# TODO sort by elevation		
def next_moves(position, map):
	moves = set()
	xmax, ymax = map.shape
	xmax -= 1
	ymax -= 1 
	elevation = map[xpos][ypos]
	if position.xpos < xmax and  elevation > map[xpos+1][ypos]:
		moves.add(Move(position, Position(xpos+1, ypos)))
	if position.xpos > 0 and  elevation > map[xpos-1][ypos]:
		moves.add(Move(position, Position(xpos-1, ypos)))
	if position.ypos > 0 and  elevation > map[xpos][ypos-1]:
		moves.add(Move(position, Position(xpos, ypos-1)))
	if position.ypos < ymax and  elevation > map[xpos][ypos+1]:
		moves.add(Move(position, Position(xpos, ypos+1)))
	
		
def depth_search(position, direction, traversed, max_distance, map, distance):
	# return if already calculated
	if distance[position.xpos][position.ypos] != -1:
		return distance[position.xpos][position.ypos]
	# return -1 if no sense in searching
	if traversed + map[position.xpos][position.ypos] < max_distance
		return -1

	moves = get_moves(position, direction, map)
	# return 0 if no moves possible
	if len(moves) == 0:
		distance[position.xpos][position.ypos] = 0
		return 0
	# recursively depth search 
	max_depth = -1
	for move in moves:
		next_position = get_position(position, move, map)
		depth = depth_search(next_position, move, traversed+1, max_distance, map, distance)
		if depth > max_depth : max_depth = depth
		
	distance[position.xpos][position.ypos] = max_depth
	return max_depth
	
	

def get_moves(position, direction, map):
	moves = set()
	xmax, ymax = map.shape
	xmax -= 1
	ymax -= 1 
	elevation = map[xpos][ypos]
	if position.xpos < xmax and  elevation > map[xpos+1][ypos]:
		moves.add(Direction.East)
	if position.xpos > 0 and  elevation > map[xpos-1][ypos]:
		moves.add(Direction.West)
	if position.ypos > 0 and  elevation > map[xpos][ypos-1]:
		moves.add(Direction.South)
	if position.ypos < ymax and  elevation > map[xpos][ypos+1]:
		moves.add(Direction.North)
	if direction is not None:
		moves.remove(direction.opposite)
	return moves
	

def is_downhill(start, end, map):
	# TODO check if out of boundary?
	xmax, ymax = map.shape
	xpos, ypos = position
	if Direction.North == direction:
		return map[xpos][ypos] > map[xpos][ypos+1]
	elif Direction.South == direction:
		return map[xpos][ypos] > map[xpos][ypos-1]
	elif Direction.East == direction:
		return map[xpos][ypos] > map[xpos+1][ypos]
	elif Direction.West == direction:
		return map[xpos][ypos] > map[xpos-1][ypos]
		
		
class Position(namedtuple('Position', 'xpos ypos')):
	def __eq__(self, other):
		return self.xpos == other.xpos and self.ypos == other.ypos
	def __eq__(self, other):
		return self.xpos == other.xpos and self.ypos == other.ypos

Move = namedtuple('Move', 'from to')

class Direction(Enum):
	North = 0
	South = 2
	East = 1
	West = 3
	
	def opposite(self):
		return Direction((self.value + 2)% )
		
class Node:
	def __init__(self, position, elevation, visited, children):
		self.position = position
		self.elevation = elevation
		self.visited = visited
		self.children = children
		
	def next():
