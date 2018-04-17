import numpy as np
from collections import namedtuple
from enum import Enum
size=5
map = np.random.randint(2*size, size=(size,size))
# initialize distance matrix with -1. Alternatively use np.NaN
distance = np.ones((size, size), dtype=np.int16)
distance = np.negative(distance)
Position = namedtuple('Position', 'xpos ypos')

Direction = Enum('Direction', 'North South East West')

class Direction(Enum):
	North = 1
	South = 2
	East = 3
	West = 4
	
	def opposite(self):
		if self.name == 'North':
			return Direction.South
		elif self.name == 'South':
			return Direction.North 
		elif self.name == 'East':
			return Direction. West
		elif self.name =='West'

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
	# return 0 if no moves possible
	moves = get_moves(position, direction, map)
	# recursively depth search 

def get_moves(position, direction, map):
	directions = get_di



