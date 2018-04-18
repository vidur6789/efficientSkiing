import numpy as np
from collections import namedtuple
from enum import Enum
size=5
map = np.random.randint(2*size, size=(size,size))
# initialize distance matrix with -1. Alternatively use np.NaN
distance = np.ones((size, size), dtype=np.int16)
distance = np.negative(distance)
			

Direction = Enum('Direction', 'North South East West')

class Direction(Enum):
	North = 1
	South = -1
	East = 2
	West = -2
	
	def opposite(self):
		return Direction(-self.value)

for (i in range(size)):
	for(j in range(size)):
		position = Position(i, j)
		traversed=0
		max_distance=0	
		ski_distance = depth_search(position, traversed, max_distance, map, distance)
		max_distance = ski_distance if ski_distance > max_distance else max_distance # TODO tie breaker
		
		
def depth_search(position, direction, traversed, max_distance, map, distance):
	# return if already calculated
	if distance[position.xpos][position.ypos] != -1:
		return distance[position.xpos][position.ypos]
	# return -1 if no sense in searching
	if traversed + map[position.xpos][position.ypos] < max_distance
		return -1

	moves = get_moves(position, direction, map)
	# return 0 if no moves possible
	if len(a) == 0:
		distance[position.xpos][position.ypos] = 0
		return 0
	# recursively depth search 
	max_depth = -1
	for move in moves:
		next_position = get_position(position, move, map)
		depth = depth_search(next_position, move, traversed+1, max_distance, map, distance)
		if depth > max_depth : max_depth = depth
		
	distance[position.xpos][position.ypos] = max_depth
	
	

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
	

def is_downhill(position, direction, map):
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
