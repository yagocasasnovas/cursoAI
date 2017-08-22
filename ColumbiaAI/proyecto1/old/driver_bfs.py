
import sys
import math
import timeit
import resource

"""sys.stdout = open('output.txt', 'w')"""

"""Functions and classes"""


def CheckDimensionOfBoard(StartState):
	
	length = len(StartState.replace(',',''))
	
	return math.sqrt(length)
	



	

def GetPossibleMovements(state,dimension):
	
	output = []
	
	state = list(state)
	
	dimensiontosquare = int(dimension * dimension)
	
	"""find zero"""
	position = state.index('0')
	
	y0 = int(position/dimension)
	x0 = position % dimension
	
	"""find each number position"""
	up   = int(x0 + dimension*(y0-1))
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






SearchAlgorithm = sys.argv[1]

StartState = sys.argv[2]

board_dimension = CheckDimensionOfBoard(StartState)

StartState = StartState.split(',')

StartState = tuple(StartState)

StartStateNode = ('',StartState)


"""GoalState = ('',('0','1','2','3','4','5','6','7','8'))"""
GoalState = ('0','1','2','3','4','5','6','7','8')


if SearchAlgorithm == 'dfs':

	"Algorithm for DFS"
	
	stack = Stack()

	visible = set()
	route_temp = dict = {}
	route = Queue()

	stack.push(StartState)

	iteration = 0
	max_fringe = 0
	max_depth = 0
	depth = 0
	
	while stack:
		
		
		
		nodeValue = stack.pop()

		"""nodeValue = node[1]"""
		

		
		
		if nodeValue == GoalState:
						
			act = nodeValue
			while (act != StartState):
				route.push(dict[act][1])
				act = dict[act][0]
					
			print 'path_to_goal: ' + str(route.list)
			print 'cost_of_path: ' + str(route.isLong())
			print 'nodes_expanded: ' + str(iteration)
			print 'fringe_size: ' + str(stack.isLong())
			print 'max_fringe_size: ' + str(max_fringe)
			print 'search_depth: ' + str(max_depth)
			print 'max1_search_depth ' + str(depth)
			print 'ss'
			break

		if nodeValue not in visible:
			
			visible.add(nodeValue)
			for childnode in GetPossibleMovements(nodeValue,board_dimension):
				
				if childnode[1] not in visible and childnode[1] not in stack.list:

					stack.push(childnode[1])
					depth = depth + 1
					dict[childnode[1]] = (nodeValue,childnode[0])
					

					
					



		if max_fringe < stack.isLong():
			max_fringe = stack.isLong()
		if max_depth < depth:
			max_depth = depth
		iteration = iteration + 1



if SearchAlgorithm == 'bfs':

	start_bfs = timeit.default_timer()

	"Algorithm for BFS"
	
	stack = Queue()

	visible = set()
	route_temp = dict = {}
	route = Queue()

	stack.push(StartState)

	iteration = 0
	max_fringe = 0
	max_depth = 0
	depth = 0
	
	while stack:
		
		
		
		nodeValue = stack.pop()

		"""nodeValue = node[1]"""
		

			
		
		if nodeValue == GoalState:
						
			act = nodeValue
			while (act != StartState):
				route.push(dict[act][1])
				act = dict[act][0]
				stop_bfs = timeit.default_timer()
				time_bfs = stop_bfs - start_bfs
			print 'path_to_goal: ' + str(route.list)
			print 'cost_of_path: ' + str(route.isLong())
			print 'nodes_expanded: ' + str(len(visible))
			print 'fringe_size: ' + str(stack.isLong())
			print 'max_fringe_size: ' + str(max_fringe)
			print 'search_depth: ' + str(depth)
			print 'max_search_depth: ' + str(max_depth)
			print 'running_time: ' + str(time_bfs)
			print 'max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / float(1000))
			
			break
		
		print iteration
		
		if nodeValue not in visible:
			
			visible.add(nodeValue)
			for childnode in GetPossibleMovements(nodeValue,board_dimension):
				print childnode
				if childnode[1] not in visible and childnode[1] not in stack.list:

					stack.push(childnode[1])
					depth = depth + 1
					dict[childnode[1]] = (nodeValue,childnode[0])
					print stack.list

					
					



		if max_fringe < stack.isLong():
			max_fringe = stack.isLong()
		if max_depth < depth:
			max_depth = depth
		iteration = iteration + 1
		
	








