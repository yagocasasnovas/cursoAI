
import sys
import math
from __future__ import print_function


"""Functions and classes"""

def CheckDimensionOfBoard(StartState):
	
	length = len(StartState.replace(',',''))
	
	return math.sqrt(length)
	

def executeGoal():
		print "Goal"
		

def order(a):
	k = ['U','D','L','R']
	
	
	

def GetPossibleMovements(state,dimension):
	
	output = []
	
	
	
	state = list(state)
	
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

	if x0 >= 0 and x0 < dimension-1:
		rightvalue = state[right]
		rightstate = state[:]
		rightstate[right] = '0'
		rightstate[position] = rightvalue
		output.append(('R',tuple(rightstate))) 

	if x0 >= 1 and x0 < dimension:
		leftvalue = state[left]
		leftstate = state[:]
		leftstate[left] = '0'
		leftstate[position] = leftvalue
		output.append(('L',tuple(leftstate))) 
		

	if y0 >= 0 and y0 < dimension-1:
		downvalue = state[down]
		downstate = state[:]
		downstate[down] = '0'
		downstate[position] = downvalue
		output.append(('D',tuple(downstate))) 

	if y0 >= 1 and y0 < dimension :
		upvalue = state[up]
		upstate = state[:]
		upstate[up] = '0'
		upstate[position] = upvalue
		output.append(('U',tuple(upstate))) 
	
	

	

		

	
	return output


StartState = sys.argv[1]

board_dimension = CheckDimensionOfBoard(StartState)

StartState = StartState.split(',')

StartState = tuple(StartState)

StartStateNode = ('',StartState)


print GetPossibleMovements(StartState	,board_dimension)








