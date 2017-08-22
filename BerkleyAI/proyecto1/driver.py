
import sys
import math
import timeit
import resource
 
 
"""sys.stdout = open('output.txt', 'w')"""
 
"""Functions and classes"""


def ManhattanDistance(state,goalstate,dimension):
	manhattan_distance = 0
	dimension = int(dimension)
	index_state = 0
	for a in state:
		index_goal = 0
		for b in goalstate:
			if a == b and b != '0':
				
				manhattan_distance = manhattan_distance + abs((index_goal % dimension) - (index_state % dimension)) + abs(int(index_goal/dimension) - int(index_state/dimension))
				print 'index_state ' + str(index_state) + ' index_goal ' + str(index_goal) + ' value_state ' + str(a) + ' value_goal ' + str(b) + ' : ' + str(manhattan_distance) + ' ' + str(abs((index_goal % dimension) - (index_state % dimension)) + abs(int(index_goal/dimension) - int(index_state/dimension)))
			index_goal = index_goal +1
		index_state = index_state +1
		

	return manhattan_distance
 
def DefineGoalState(dimension):
 
	dimension = int(dimension)*int(dimension)
	g = [str(x).zfill(1) for x in range(dimension)]
	h = tuple(g)

	"""h = ('8', '4', '6', '2', '3', '1', '0', '5', '7')"""
	
	return h


 
def CheckDimensionOfBoard(StartState):

	length = len(StartState.replace(',',''))

	return math.sqrt(length)

 
def GetPossibleMovementsBFS(state,dimension):

	output = []

	state = list(state)

	dimension = int(dimension)

	dimensiontosquare = int(dimension * dimension)

	"""find zero"""
	position = state.index('0')

	y0 = int(position/dimension)
	x0 = int(position % dimension)


	"""find each number position"""
	up   = int(x0 + dimension*(y0-1))
	down = int(x0 + dimension*(y0+1))
	left = int(x0-1 + dimension*y0)
	right = int(x0+1 + dimension*y0)


	"""Get each of new states"""


	if y0 >= 1 and y0 < dimension :
		upvalue = state[up]
		upstate = state[:]
		upstate[up] = '0'
		upstate[position] = upvalue
		output.append(('Up',tuple(upstate)))


	if y0 >= 0 and y0 < dimension-1:
		downvalue = state[down]
		downstate = state[:]
		downstate[down] = '0'
		downstate[position] = downvalue
		output.append(('Down',tuple(downstate)))

	if x0 >= 1 and x0 < dimension:
		leftvalue = state[left]
		leftstate = state[:]
		leftstate[left] = '0'
		leftstate[position] = leftvalue
		output.append(('Left',tuple(leftstate)))

	if x0 >= 0 and x0 < dimension-1:
		rightvalue = state[right]
		rightstate = state[:]
		rightstate[right] = '0'
		rightstate[position] = rightvalue
		output.append(('Right',tuple(rightstate)))

	return output


def GetPossibleMovementsDFS(state,dimension):
	output = []

	state = list(state)

	dimension = int(dimension)
               
	dimensiontosquare = int(dimension * dimension)
               
	"""find zero"""
	position = int(state.index('0'))
               
	y0 = int(position/dimension)
	x0 = int(position % dimension)
               
	"""find each number position"""
	up = int(x0 + dimension*(y0-1))
	down = int(x0 + dimension*(y0+1))
	left = int(x0-1 + dimension*y0)
	right = int(x0+1 + dimension*y0)


	"""Get each of new states"""
 
	if x0 >= 0 and x0 < dimension-1:
		rightvalue = state[right]
		rightstate = state[:]
		rightstate[right] = '0'
		rightstate[position] = rightvalue
		output.append(('Right',tuple(rightstate)))
 
	if x0 >= 1 and x0 < dimension:
		leftvalue = state[left]
		leftstate = state[:]
		leftstate[left] = '0'
		leftstate[position] = leftvalue
		output.append(('Left',tuple(leftstate)))

 
	if y0 >= 0 and y0 < dimension-1:
		downvalue = state[down]
		downstate = state[:]
		downstate[down] = '0'
		downstate[position] = downvalue
		output.append(('Down',tuple(downstate)))
 
	if y0 >= 1 and y0 < dimension :
		upvalue = state[up]
		upstate = state[:]
		upstate[up] = '0'
		upstate[position] = upvalue
		output.append(('Up',tuple(upstate)))
               
               
               
	return output
 
class Stack:
	"A container with a LIFO queuing policy."
	def __init__(self):
		self.list = []

	def push(self,item):
		"Push item in the stack"
		self.list.append(item)

	def pop(self):
		"Pop the most recently pushed item from the stack"
		return self.list.pop()

	def isEmpty(self):
		"Returns true if the stack is empty"
		return len(self.list) == 0

	def isLong(self):
		"Returns length of queue"
		return len(self.list)

class Queue:
	"A container with a first-in-first-out (FIFO) queuing policy."
	def __init__(self):
		self.list = []

	def push(self,item):
		"Enqueue the 'item' into the queue"
		self.list.insert(0,item)

	def pop(self):
		"""
		Dequeue the earliest enqueued item still in the queue. This
		operation removes the item from the queue.
		"""
		return self.list.pop()

	def isEmpty(self):
		"Returns true if the queue is empty"
		return len(self.list) == 0

	def isLong(self):
		"Returns length of queue"
		return len(self.list)
 
start = timeit.default_timer()
 
SearchAlgorithm = sys.argv[1]
 
StartState = sys.argv[2]
 
board_dimension = CheckDimensionOfBoard(StartState)
 
StartState = StartState.split(',')
 
StartState = tuple(StartState)
 
StartStateNode = ('',StartState)
 

"""GoalState = ('0','1','2','3','4','5','6','7','8')"""
GoalState = DefineGoalState(board_dimension)
 
"""GoalState = ('4', '0', '5', '6', '8', '1', '3', '2', '7')"""
 
 
if SearchAlgorithm == 'dfs':
               

 
	"Algorithm for DFS"
               
	stack = Stack()

	visible = set()
	lookup = set()
	depth = {StartState:0}
	route_temp = {}
	route = Queue()
 
	stack.push(StartState)

	iteration = 0
	max_fringe = 0
	max_depth = 0
               
               
	while stack:



		nodeValue = stack.pop()
	
                              
 
 
		"""nodeValue = node[1]"""
                              
		if nodeValue == GoalState:
		
			act = nodeValue
			while (act != StartState):
				route.push(route_temp[act][1])
				act = route_temp[act][0]
				stop = timeit.default_timer()
				time = stop - start              
                                                              
			if max_depth < depth[nodeValue]:
				max_depth = depth[nodeValue]
			print 'path_to_goal: ' + str(route.list)
			print 'cost_of_path: ' + str(route.isLong())
			print 'nodes_expanded: ' + str(len(visible))
			print 'fringe_size: ' + str(stack.isLong())
			print 'max_fringe_size: ' + str(max_fringe)
			print 'search_depth: ' + str(depth[nodeValue])
			print 'max_search_depth: ' + str(max_depth)
			print 'running_time: ' + str(time)
			print 'max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / float(1024))
			break
 
		if nodeValue not in visible:
                                              
			visible.add(nodeValue)
 
			for childnode in GetPossibleMovementsDFS(nodeValue,board_dimension):
                                                              
				if childnode[1] not in visible and childnode[1] not in lookup:
 
					stack.push(childnode[1])
 					lookup.add(childnode[1])
					route_temp[childnode[1]] = (nodeValue,childnode[0])
					depth[childnode[1]] = depth[nodeValue] + 1
                                                                             
		if max_fringe < stack.isLong():
			max_fringe = stack.isLong()
		if max_depth < depth[childnode[1]]:
			max_depth = depth[childnode[1]]
		iteration = iteration + 1

 
 
GoalState = ('0','1','2','3','4','5','6','7','8')
GoalState = DefineGoalState(board_dimension)
 
if SearchAlgorithm == 'bfs':
 

 
	"Algorithm for BFS"

	stack = Queue()
	depth = {StartState:0}
	visible = set()
	route_temp = {}
	route = Queue()
 
	stack.push(StartState)
 
	iteration = 0
	max_fringe = 0
	max_depth = 0
 
               
	while stack:
                              
                              
                              
		nodeValue = stack.pop()
                              
                              
                              
		if nodeValue == GoalState:
                                                                                             
			act = nodeValue
			while (act != StartState):
				route.push(route_temp[act][1])
				act = route_temp[act][0]
				stop = timeit.default_timer()
				time = stop - start
			if max_depth < depth[nodeValue]:
				max_depth = depth[nodeValue]
			print 'path_to_goal: ' + str(route.list)
			print 'cost_of_path: ' + str(route.isLong())
			print 'nodes_expanded: ' + str(len(visible))
			print 'fringe_size: ' + str(stack.isLong())
			print 'max_fringe_size: ' + str(max_fringe)
			print 'search_depth: ' + str(route.isLong())
			print 'max_search_depth: ' + str(max_depth)
			print 'running_time: ' + str(time)
 
			print 'max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / float(1024))
                                              
			break
                              
                              
                              
		if nodeValue not in visible and nodeValue not in stack.list:
                                              
			visible.add(nodeValue)
 
			for childnode in GetPossibleMovementsBFS(nodeValue,board_dimension):
                                                              
				if childnode[1] not in visible and childnode[1] not in stack.list:
 
					stack.push(childnode[1])
 
					route_temp[childnode[1]] = (nodeValue,childnode[0])
					depth[childnode[1]] = depth[nodeValue] + 1
                                                              
                                                                             
		if max_fringe < stack.isLong():
			max_fringe = stack.isLong()
		if max_depth < depth[childnode[1]]:
			max_depth = depth[childnode[1]]
		iteration = iteration + 1



GoalState = DefineGoalState(board_dimension)

 
if SearchAlgorithm == 'ast':
	
	"Algorithm for A STAR"
	
	print ManhattanDistance(StartState,GoalState,board_dimension)
	
	
	
	
	
	
	
	
	
	
	
	
	
	



 