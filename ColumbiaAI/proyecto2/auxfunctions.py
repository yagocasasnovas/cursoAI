
	
def returnvalidmovement(node):
	
	moves1 = node.getAvailableMoves()
	
	if moves1[0] == 0:
		return 0
	
	else:
		if moves1[0] == 1 and moves1[1] == 2:
			return 2
		else:
			return moves1[0]
	
def expandMin(node):

	grid_temp = []
	grid_temp_index = 0

	
	for indexColumn, column in enumerate(node.map):
		for indexRow, row in enumerate(column):
			if(node.canInsert([indexColumn,indexRow])):
				
				grid_temp.append(node.clone())
				grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)

				grid_temp_index +=1
	
#	for indexColumn, column in enumerate(node.map):
#		for indexRow, row in enumerate(column):
#			if(node.canInsert([indexColumn,indexRow])):
#				
#				grid_temp.append(node.clone())
#				grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],4)
#
#				grid_temp_index +=1
	
	
	return grid_temp

def expandMin2(node):
	
	j = 0
	grid_temp = []
	grid_temp_index = 0

	for indexColumn, column in enumerate(node.map):
		for indexRow, row in enumerate(column):
			if(node.canInsert([indexColumn,indexRow])):
				
				grid_temp.append(node.clone())
				grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)

				j = 1
			if j == 1:
				break
		if j == 1:
			break
		

	

	
	
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
		grid_temp.append((node.clone(),a))

		grid_temp[grid_temp_index][0].move(a)
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


def exampleGrid3(grid):
	exampleGrid_temp = grid.clone()
	for indexColumn, column in enumerate(exampleGrid_temp.map):
		for indexRow, row in enumerate(column):
			
			exampleGrid_temp.insertTile([indexColumn,indexRow],0)

	
	exampleGrid_temp.insertTile([0,0],4)
	exampleGrid_temp.insertTile([1,0],128)
	exampleGrid_temp.insertTile([2,0],8)
	exampleGrid_temp.insertTile([3,0],2)
	exampleGrid_temp.insertTile([0,1],128)
	exampleGrid_temp.insertTile([1,1],2)
	exampleGrid_temp.insertTile([2,1],64)
	exampleGrid_temp.insertTile([3,1],16)
	exampleGrid_temp.insertTile([0,2],4)
	exampleGrid_temp.insertTile([1,2],32)
	exampleGrid_temp.insertTile([2,2],8)
	exampleGrid_temp.insertTile([3,2],4)
	exampleGrid_temp.insertTile([0,3],8)
	exampleGrid_temp.insertTile([1,3],4)
	exampleGrid_temp.insertTile([2,3],2)
	exampleGrid_temp.insertTile([3,3],0)
	return exampleGrid_temp



	
	
	
	
	
def pretty_print(grid):
	
	print
	for indexColumn, column in enumerate(grid.map):
		
		print str(column[0])+'   '+str(column[1])+'   '+str(column[2])+'   '+str(column[3])
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
		
		
	