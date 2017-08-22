""" test """
"""2 sale con 90% y 4 con 10%"""


from BaseAI import BaseAI
import time
 
class PlayerAI(BaseAI):
	
	
	
	def getMove(self, grid):
		
		t = time.clock()
		
		




		j = self.decision(grid,3)
		
		if j is None:
			
			j = self.decision(grid,2)
			
			if j is None:
				
				j = self.decision(grid,1)

		for a in self.expandMaxDir(grid):
			if j.map == a[0].map:

				defmove = a[1]
				print("--- %s seconds ---" % (time.clock() - t))
				return defmove
			
		
		

		"""print defmove"""
		
		"""raw_input("Press Enter to continue...")"""
		"""return moves[randint(0, len(moves) - 1)] if moves else None"""
		
	
	def heuristic(self,node):
	
		"""calcular heuristica nodo"""
		node_temp = node.clone()
		maxTile = node_temp.getMaxTile()
		KmaxTile = 1
		freeCells = len(node_temp.getAvailableCells())
		KfreeCells = 1000
		AvailableMoves = len(node_temp.getAvailableMoves())
		KAvailableMoves = 1
		ValuesCorners = self.valuesInCorners(node)
		KValuesCorners = 1
		MaxValueCorners = self.maxValueCorners(node)
		KMaxValueCorners = 100
		kspread = 5
		kspread2 = 5
		leftcell = self.leftcellf(node)
		kleftcell = 1000
		
		return kspread2*self.spread2(node) + KfreeCells*freeCells + kleftcell*leftcell
		"""return maxTile*KmaxTile + freeCells*KfreeCells + AvailableMoves*KAvailableMoves + KValuesCorners * ValuesCorners + KMaxValueCorners*MaxValueCorners"""
		
	
		


	def expandMin(self,node):
	
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
	
	
	def expandMax(self,node):
	
		grid_temp = []
		grid_temp_index = 0
	
	
		moves = node.getAvailableMoves()
		for a in moves:
			grid_temp.append(node.clone())

			grid_temp[grid_temp_index].move(a)
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



	def GoalState(self,node):
	
		"""goalState"""
	
	
		if node.getMaxTile == 256:
			return True
	
		return False


	def exampleGrid(self,grid):
		exampleGrid_temp = grid.clone()
		for indexColumn, column in enumerate(exampleGrid_temp.map):
			for indexRow, row in enumerate(column):
				
				exampleGrid_temp.insertTile([indexColumn,indexRow],0)

		
		exampleGrid_temp.insertTile([0,1],2)
		exampleGrid_temp.insertTile([0,2],4)
		return exampleGrid_temp





	def leftcellf(self,node):
		
		a = -1
		if node.getCellValue([0,3]) == 0:
			return a
			
		return 1
	
	
	def valuesInCorners(self,node):
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

	def maxValueCorners(self,node):

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
		
		
	def spread2(self,node):
		

		
		if node.getMaxTile() == node.getCellValue([0,1]) and node.getMaxTile() != node.getCellValue([0,0]) and node.getMaxTile() > 16:
			
			a1 = 500
			a2 = 80
			a3 = 60
			a4 = 40
			b1 = 80
			b2 = 40
			b3 = 20
			b4 = 10
			c1 = 1
			c2 = 2
			c3 = 3
			c4 = 4
			d1 = 0
			d2 = 0
			d3 = 0
			d4 = 0
			
		else:
			
			a1 = 500
			a2 = 80
			a3 = 60
			a4 = 40
			b1 = 5
			b2 = 10
			b3 = 20
			b4 = 30
			c1 = 4
			c2 = 3
			c3 = 2
			c4 = 1
			d1 = 0
			d2 = 0
			d3 = 0
			d4 = 0
		
		filaa = a1*node.getCellValue([0,0]) + a2*node.getCellValue([0,1]) + a3*node.getCellValue([0,2]) + a4*node.getCellValue([0,3])
		filab = b1*node.getCellValue([1,0]) + b2*node.getCellValue([1,1]) + b3*node.getCellValue([1,2]) + b4*node.getCellValue([1,3])
		filac = c1*node.getCellValue([2,0]) + c2*node.getCellValue([2,1]) + c3*node.getCellValue([2,2]) + c4*node.getCellValue([2,3])
		filad = d1*node.getCellValue([3,0]) + d2*node.getCellValue([3,1]) + d3*node.getCellValue([3,2]) + d4*node.getCellValue([3,3])
		
		return filaa + filab + filac + filad
		
	def together(self,node):
		
		
		
		return


	def abmaximize(self,node,alpha,beta, depth):
		
		
		if self.GoalState(node) or depth == 0:
			return ( None ,self.heuristic(node))
			
		maxUtility = -999999
		maxChild = None
			
		for child in self.expandMax(node):
			
			(_,utility) = self.abminimize(child,-999999,999999, depth - 1)
			
			if utility > maxUtility:
				(maxChild, maxUtility) = (child, utility)
				
			if maxUtility >= beta:
				break
				
			if maxUtility > alpha:
				alpha = maxUtility
		
		return (maxChild,maxUtility)





	def abminimize(self, node, alpha, beta, depth):


		if depth == 0:
			return (None,self.heuristic(node))
		
		minUtility = 999999
		minChild = None
		
		for child in self.expandMin(node):
			
			(_,utility) = self.abmaximize(child,-999999,999999, depth - 1)
			
			if utility < minUtility:
				(minChild,minUtility) = (child,utility)
			
			if minUtility <= alpha:
				break
			
			if minUtility < beta:
				beta = minUtility
			
			
		return (minChild, minUtility)


	def decision(self, node, depth):
		
		(child, _ ) = self.abmaximize(node,-999999,999999, depth)
		
		return child


	