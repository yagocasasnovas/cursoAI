
import sys
import math
import timeit
import resource
import heapq
 
 
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

			index_goal = index_goal +1
		index_state = index_state +1
		

	return manhattan_distance
 
def DefineGoalState(dimension):
 
	dimension = int(dimension)*int(dimension)
	g = [str(x).zfill(1) for x in range(dimension)]
	h = tuple(g)

	"""h = ('8', '4', '6', '2', '3', '1', '0', '5', '7')"""
	
	return h


 
def CheckDimensionOfBoard(state_temp):


	length = len(state_temp.replace(',',''))

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
	
	
	
	

 
def GetPossibleMovementsAST(state,dimension):

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


class PriorityQueue:

	def __init__(self):
		self.listitems = []

		self.count = 0
		

		

	def isEmpty(self):
 		
 		return self.count == 0
 		
 	def push(self,item,cost,direction):
 		if direction == 'Up' or direction == '':
 			direction1 = 0
 		if direction == 'Down':
 			direction1 = 1
 		if direction == 'Left':
 			direction1 = 2
 		if direction == 'Right':
 			direction1 = 3
 		self.listitems.append((item,cost,direction,direction1))
 		self.count = self.count + 1
 		
 	def pop(self):
 		self.count = self.count - 1
 		return self.listitems.pop()[0]


	def order(self):
		
		
		"""print 'antes ' + str(self.listitems)"""
		i = 0
		for item in self.listitems:
			j = 0
			for item2 in self.listitems:

				if item2[1] < item[1]:
					self.listitems[i] = item2
					self.listitems[j] = item
					break
				j = j + 1
			i = i + 1
		"""print 'despues ' + str(self.listitems)"""
		i = 0
		for item in self.listitems:
			j = 0
			for item2 in self.listitems:

				if item2[1] == item[1]:
					if item2[3] > item[3]:
						self.listitems[i] = item2
						self.listitems[j] = item
						break
				j = j + 1
			i = i + 1





start = timeit.default_timer()
 
SearchAlgorithm = sys.argv[1]
 
StartState = sys.argv[2]

board_dimension = CheckDimensionOfBoard(StartState) 
 
StartState = StartState.split(',')
 
StartState = tuple(StartState)
 
StartStateNode = ('',StartState)



GoalState = DefineGoalState(board_dimension)
 

 
 
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


		stack.order()
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





 
if SearchAlgorithm == 'ast':
	
	"Algorithm for A STAR"
	
	iteration = 0
	stack = PriorityQueue()
	depth = {StartState:0}
	stack.push(StartState,0,'')
	visible = set()
	route_temp = {}
	route = Queue()
	
	
	cost = {}
	max_fringe = 0
	max_depth = 0
	route_temp[StartState] = None

	cost[StartState] = 0
	
	i = 0
	
	while stack:
	
		
		stack.order()
		nodeValue = stack.pop()
		"""print 't: ' + str(nodeValue)"""
		
		
		
		
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
			print 'fringe_size: ' + str(stack.count)
			print 'max_fringe_size: ' + str(max_fringe)
			print 'search_depth: ' + str(route.isLong())
			print 'max_search_depth: ' + str(max_depth)
			print 'running_time: ' + str(time)
 
			print 'max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / float(1024))

                                              
			break
			
		visible.add(nodeValue)
		priorities = list()
		mincost = list()
		j = 0
		for childnode in GetPossibleMovementsAST(nodeValue,board_dimension):
			cost_temp = cost[nodeValue] + 1
			if childnode[1] not in cost or cost_temp < cost[childnode[1]]:
				cost[childnode[1]] = cost_temp
				fcost = cost_temp + ManhattanDistance(childnode[1],GoalState,board_dimension)
				stack.push(childnode[1],fcost,childnode[0])
				
				route_temp[childnode[1]] = (nodeValue,childnode[0])
				depth[childnode[1]] = depth[nodeValue] + 1
		
			"""print str(nodeValue) + ' ' + str(childnode) + ' ' + str(fcost)"""


		
		if i == 1000000:
			break
		i = i + 1
		
		if max_fringe < stack.count:
			max_fringe = stack.count
		if max_depth < depth[childnode[1]]:
			max_depth = depth[childnode[1]]

		iteration = iteration + 1


 