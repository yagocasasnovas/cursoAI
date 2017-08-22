
import sys
import math
import timeit
import resource
import heapq
 
 
"""sys.stdout = open('output.txt', 'w')"""
 
"""Functions and classes"""

def print_cube(node):

	print '-----'
	print '|' + str(node[0]) + str(node[1]) + str(node[2]) + '|'
	print '|' + str(node[3]) + str(node[4]) + str(node[5]) + '|'
	print '|' + str(node[6]) + str(node[7]) + str(node[8]) + '|'
	print '-----'


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

def udlr_to_number(direction):
	if direction == 'Up':
		out = 0
	if direction == 'Down':
		out = 1
	if direction == 'Left':
		out = 2
	if direction == 'Right':
		out = 3
	
	return out


def udlr_to_number_inverse(direction):
	if direction == 'Up':
		out = 3
	if direction == 'Down':
		out = 2
	if direction == 'Left':
		out = 1
	if direction == 'Right':
		out = 0
	
	return out


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


class PriorityQueue:



    def  __init__(self):
        self.heap = []
        self.count = 0
        self.updates = 0
        self.pqlen = len(self.heap)


    def push(self, item, priority):
        entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count = self.count + 1
        

    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        self.count = self.count - 1
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        
        
        for index, (p, i) in enumerate(self.heap):
            """print 'id: ' + str(id) + ' index: ' + str(index) + ' p: ' + str(p) + ' i: ' + str(i)"""
            
            
            if i[2] == item[2]:
                
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, item))
                heapq.heapify(self.heap)
                self.updates = self.updates + 1
                
                
                break


start = timeit.default_timer()
 
SearchAlgorithm = sys.argv[1]
 
StartState = sys.argv[2]

board_dimension = CheckDimensionOfBoard(StartState) 
 
StartState = StartState.split(',')
 
StartState = tuple(StartState)
 
StartStateNode = ('',StartState)



GoalState = DefineGoalState(board_dimension)
 



 
if SearchAlgorithm == 'ida':



	
	"Algorithm for ITERATIVE DEEP A STAR"
		

	iterationloop = True
	
	iterationF = ManhattanDistance(StartState,GoalState,board_dimension)
	
	iteration1 = 0
	
	totalNodesExpanded = 0
	
	
	while iterationloop is True:
		
		iteration = 0


		
		"""stack DFS """
		stack = Stack()
		
		"""Nodos en frontera"""
		open_nodes = set()	
		
		"""Nodos visitados"""
		closed_nodes = set()
		
		outside_nodes = set()
		
		dict_nodes = {}
		"""list: fcost [0], cost[1], depth[2], route_back[3], id[4], direction[5]"""
		
		
		"""Ruta inversa"""
		route_temp = {}
		route = Queue()
		
		node_id = 0

		"""inicializaciones"""
		stack.push(StartState)
	

	
		dict_nodes[StartState] = [0,0,0,0,0,'']
		
		minimumrest = set()




		iterationloop = True
	
		max_fringe = 0
		max_depth = 0
		route_temp[StartState] = None
	
	
	
	
	
		print totalNodesExpanded
		
		
		while stack:

			
			

			
			if stack.isEmpty():
				iterationF = min(minimumrest)
				totalNodesExpanded = totalNodesExpanded + len(closed_nodes)
				
				
				break
			
			
			
			
			
			nodeValue = stack.pop()

			
			


			"""print_cube(nodeValue)"""
				
		
			if nodeValue == GoalState:
                                                                                             
				act = nodeValue
				while (act != StartState):
					route.push(dict_nodes[act][3][1])
					act = dict_nodes[act][3][0]
					stop = timeit.default_timer()
					time = stop - start
				if max_depth < dict_nodes[nodeValue][2]:
					max_depth = dict_nodes[nodeValue][2]
				print 'path_to_goal: ' + str(route.list)
				print 'cost_of_path: ' + str(route.isLong())
				print 'nodes_expanded: ' + str(totalNodesExpanded)
				"""print 'fringe_size: ' + str(stack.count)"""
				print 'fringe_size: ' + str(len(stack.list))	
				print 'max_fringe_size: ' + str(max_fringe)
				print 'search_depth: ' + str(route.isLong())
				print 'max_search_depth: ' + str(max_depth)
				print 'running_time: ' + str(time)
 			
				print 'max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / float(1024))
				iterationloop = False


				break
		
		
			if nodeValue not in closed_nodes:
                                              
				closed_nodes.add(nodeValue)
 				cost_temp = dict_nodes[nodeValue][1] + 1
 			
			
 			
				for childnode in GetPossibleMovementsDFS(nodeValue,board_dimension):

					"""si no habia visto antes el nodo"""
					if childnode[1] not in open_nodes and childnode[1] not in outside_nodes and childnode[1] not in closed_nodes:

						
						"""list: fcost [0], cost[1], depth[2], route_back[3], id[4], direction[5]"""
						
						"""establezco coste"""
 						dict_nodes[childnode[1]] = [0,cost_temp,0,0,0,childnode[0]]
 						
 						
 						"""calculo F"""
	 					fcost = cost_temp + ManhattanDistance(childnode[1],GoalState,board_dimension)
 						
 						
 						
 						if fcost <= iterationF:
 							
 							"""print str(childnode[1]) + ' F: ' + str(fcost)"""
 							"""guardo F"""
 							dict_nodes[childnode[1]][0] = fcost
 						
 												
 							"""print childnodeTuple"""
							stack.push(childnode[1])
						
							"""anyado a open"""
  							open_nodes.add(childnode[1])
  						
  							"""guardo ruta"""
  						
  							dict_nodes[childnode[1]][3] = (nodeValue,childnode[0])
  						
							"""route_temp[childnode[1]] = (nodeValue,childnode[0])"""
						
							"""guardo depth"""
						
							dict_nodes[childnode[1]][2] = dict_nodes[nodeValue][2] + 1
						
						if fcost > iterationF:
							
							minimumrest.add(fcost)
							outside_nodes.add(childnode[1])
							
					
				if max_fringe < len(stack.list):
					max_fringe = len(stack.list)
				if max_depth < dict_nodes[childnode[1]][2]:
					max_depth = dict_nodes[childnode[1]][2]
			iteration = iteration + 1
		iteration1 = iteration1 = 0

		"""raw_input("Press Enter to continue...")"""







 