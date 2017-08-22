





plus_infinite = 9999999
minus_infinite = -9999999
alphaclass = 123
betaclass = 123
	
	
def heuristic(node):

	"""calcular heuristica nodo"""
	node_temp = node.clone()
	maxTile = node_temp.getMaxTile()
	KmaxTile = 1
	freeCells = len(node_temp.getAvailableCells())
	KfreeCells = 100
	AvailableMoves = len(node_temp.getAvailableMoves())
	KAvailableMoves = 1
	ValuesCorners = valuesInCorners(node)
	KValuesCorners = 1
	MaxValueCorners = maxValueCorners(node)
	KMaxValueCorners = 100
	kspread = 5
	kspread2 = 5
	totalCountValue = totalCount(node)
	
	j = 0
	
	if node.map == exampleGrid2(node).map:
		j = 50
	"""return kspread2*spread2(node) + KfreeCells*freeCells"""
	"""return maxTile*KmaxTile + freeCells*KfreeCells + AvailableMoves*KAvailableMoves + KValuesCorners * ValuesCorners + KMaxValueCorners*MaxValueCorners"""
	"""return freeCells + maxTile + AvailableMoves + ValuesCorners + totalCountValue + j"""
	"""return totalCountValue"""
	return maxTile
	
	
	

	
	
	
	
def expandMin(node):

	grid_temp = []
	grid_temp_index = 0

	
	for indexColumn, column in enumerate(node.map):
		for indexRow, row in enumerate(column):
			if(node.canInsert([indexColumn,indexRow])):
				
				grid_temp.append(node.clone())
				grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)

				grid_temp_index +=1
	
	for indexColumn, column in enumerate(node.map):
		for indexRow, row in enumerate(column):
			if(node.canInsert([indexColumn,indexRow])):
				
				grid_temp.append(node.clone())
				grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],4)

				grid_temp_index +=1
	
	
	return grid_temp


def expandMinMin(node):

	grid_temp = []
	grid_temp_index = 0

	
	for indexColumn, column in enumerate(node.map):
		for indexRow, row in enumerate(column):
			if(node.canInsert([indexColumn,indexRow]) and grid_temp_index < 2):
				
				grid_temp.append(node.clone())
				grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)

				grid_temp_index +=1
	
	
	
	return grid_temp


def expandMax(node):

	grid_temp = []
	grid_temp_index = 0


	moves = node.getAvailableMoves()

	for a in moves:
		grid_temp.append(node.clone())

		grid_temp[grid_temp_index].move(a)
		grid_temp_index += 1

	return grid_temp


def expandMax1(node):

	grid_temp = []
	grid_temp_index = 0


	moves = node.getAvailableMoves()
	
	

	for a in moves:
		grid_temp.append((node.clone(),moves_print(a)))

		grid_temp[grid_temp_index][0].move(a)
		grid_temp_index += 1

	return grid_temp


def expandMaxDir(self,node):

	grid_temp = []
	grid_temp_index = 0


	moves = node.getAvailableMoves()
	
		
	for a in moves:
		grid_temp.append((node.clone(),a))

		grid_temp[grid_temp_index][0].move(a)
		grid_temp_index += 1

	return grid_temp



def GoalState(node):

	"""goalState"""


	if node.getMaxTile == 256:
		return True

	return False


def exampleGrid(grid):
	exampleGrid_temp = grid.clone()
	for indexColumn, column in enumerate(exampleGrid_temp.map):
		for indexRow, row in enumerate(column):
			
			exampleGrid_temp.insertTile([indexColumn,indexRow],0)

	
	exampleGrid_temp.insertTile([0,0],32)
	exampleGrid_temp.insertTile([0,1],8)
	exampleGrid_temp.insertTile([0,2],8)
	exampleGrid_temp.insertTile([1,0],4)
	exampleGrid_temp.insertTile([2,0],4)
	exampleGrid_temp.insertTile([2,2],2)
	return exampleGrid_temp



def exampleGrid2(grid):
	exampleGrid_temp = grid.clone()
	for indexColumn, column in enumerate(exampleGrid_temp.map):
		for indexRow, row in enumerate(column):
			
			exampleGrid_temp.insertTile([indexColumn,indexRow],0)

	
	exampleGrid_temp.insertTile([2,0],32)
	exampleGrid_temp.insertTile([3,0],8)
	exampleGrid_temp.insertTile([2,1],2)
	exampleGrid_temp.insertTile([3,1],8)
	exampleGrid_temp.insertTile([2,2],8)
	exampleGrid_temp.insertTile([3,2],2)
	return exampleGrid_temp



	


def valuesInCorners(node):
	a = 0
	b = 0
	c = 0
	d = 0
	
	if not node.canInsert([0,0]):
		a = 1
	if not node.canInsert([0,3]):
		b = 1
	if not node.canInsert([3,0]):
		c = 1
	if not node.canInsert([3,3]):
		d = 1

	return a + b + c + d

def maxValueCorners(node):

	maxvalue = node.getMaxTile()
	if maxvalue == node.getCellValue([0,0]) and maxvalue == node.getCellValue([0,1]):
		return 1
	if maxvalue == node.getCellValue([0,0]) and maxvalue == node.getCellValue([1,0]):
		return 1
	if maxvalue == node.getCellValue([0,3]) and maxvalue == node.getCellValue([1,3]):
		return 1
	if maxvalue == node.getCellValue([0,3]) and maxvalue == node.getCellValue([0,2]):
		return 1
	if maxvalue == node.getCellValue([3,0]) and maxvalue == node.getCellValue([3,1]):
		return 1
	if maxvalue == node.getCellValue([3,0]) and maxvalue == node.getCellValue([2,0]):
		return 1
		return 1
	if maxvalue == node.getCellValue([3,3]) and maxvalue == node.getCellValue([3,2]):
		return 1
	if maxvalue == node.getCellValue([3,3]) and maxvalue == node.getCellValue([2,3]):
		return 1




	return 0

def spread(self,node):
	
	k = 8
	i = 4
	l = 2
	a = k*node.getCellValue([0,0])
	
	b = i*node.getCellValue([0,1]) + l*node.getCellValue([0,2])
	

	
	return a + b
	
def together(self,node):
	

	
	
	return
	
	
def totalCount(node):
	
	total = 0
	for column in range(4):
		for row in range(4):
			total = total + node.getCellValue([column,row])
	
	return total
	
def spread2(node):
	
	a1 = 500
	a2 = 60
	a3 = 30
	a4 = 20
	b1 = 60
	b2 = 40
	b3 = 20
	b4 = 10
	c1 = 30
	c2 = 5
	c3 = 3
	c4 = 2
	d1 = 5
	d2 = 3
	d3 = 2
	d4 = 1
	
	filaa = a1*node.getCellValue([0,0]) + a2*node.getCellValue([0,1]) + a3*node.getCellValue([0,2]) + a4*node.getCellValue([0,3])
	filab = b1*node.getCellValue([1,0]) + b2*node.getCellValue([1,1]) + b3*node.getCellValue([1,2]) + b4*node.getCellValue([1,3])
	filac = c1*node.getCellValue([2,0]) + c2*node.getCellValue([2,1]) + c3*node.getCellValue([2,2]) + c4*node.getCellValue([2,3])
	filad = d1*node.getCellValue([3,0]) + d2*node.getCellValue([3,1]) + d3*node.getCellValue([3,2]) + d4*node.getCellValue([3,3])
	
	return filaa + filab + filac + filad
	
def together(self,node):
	
	
	
	return


def abmaximize(node,alpha,beta, depth):
	
	print
	print "---- MAXIMIZER"
	print "depth: " + str(depth)
	print "alpha: " + str(alpha)
	print "beta: " + str(beta)
	pretty_print(node)
	
	if GoalState(node) or depth == 0:
		
		print "maxheuristic: " + str(heuristic(node))
		
		raw_input("Press Enter to continue MAX leave...")
		
		return ( None ,heuristic(node))
		
	maxUtility = -999999
	maxChild = None
	

	

	m = 0
	
	for child1 in expandMax1(node):
		
		child = child1[0]
		
		print "maxloop: " + str(m)
		
		
		
		print "Direction: " + str(child1[1])
		
		"""pretty_print(child)"""
		
		(_,utility) = abminimize(child,alpha,beta, depth - 1)
		
		
		
		if utility > maxUtility:
			(maxChild, maxUtility) = (child, utility)
			
		if maxUtility >= beta:
			
			print "-----------pruning beta: " + str(maxUtility) + " " + str(beta)
			
			break
			
		if maxUtility > alpha:
			alpha = maxUtility
			
		m = m + 1
	
	"""pretty_print(node)"""
	"""print "depth: " + str(depth)"""
	"""pretty_print(maxChild)""" 
	print "Max utility: " + str(maxUtility) + " alpha: " + str(alpha) + " beta: " + str(beta)
	pretty_print(node)
	raw_input("Press Enter to continue MAX...")
	
	return (maxChild,maxUtility)





def abminimize(node, alpha, beta, depth):

	print "---- MINIMIZER"
	print "depth: " + str(depth)
	print "alpha: " + str(alpha)
	print "beta: " + str(beta)
	pretty_print(node)


	if GoalState(node) or depth == 0:
		
		print "minheuristic: " + str(heuristic(node))
		
		raw_input("Press Enter to continue MIN leave...")
		
		return ( None ,heuristic(node))
	
	minUtility = 999999
	minChild = None
	
	n = 0
	
	for child in expandMinMin(node):
		
		print "minloop: " + str(n)

		"""pretty_print(child)"""
		
		(_,utility) = abmaximize(child,alpha,beta, depth - 1)
		
		if utility < minUtility:
			(minChild,minUtility) = (child,utility)
		
		print "-----------pruning alpha: " + str(minUtility) + " " + str(alpha)
		
		if minUtility <= alpha:
			break
		
		if minUtility < beta:
			beta = minUtility
		
		n = n + 1
		
		print "Min utility: " + str(minUtility) + " alpha: " + str(alpha) + " beta: " + str(beta)
		pretty_print(node)
		raw_input("Press Enter to continue MIN...")
		
	return (minChild, minUtility)


def decision(node, depth):
	
	(child, _ ) = abmaximize(node,-999999,999999, depth)
	
	return child
	
	
	
	
	
def pretty_print(grid):
	
	print
	for indexColumn, column in enumerate(grid.map):
		
		print str(column[0])+' '+str(column[1])+' '+str(column[2])+' '+str(column[3])
		print
		
		
		
def moves_print(moveint):
	
	if moveint == 0:
		return 'UP'
	
	if moveint == 1:
		return 'DOWN'
		
	if moveint == 2:
		return 'LEFT'
		
	if moveint == 3:
		return 'RIGHT'
		
		
	