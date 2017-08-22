""" test """
"""2 sale con 90% y 4 con 10%"""

from random import randint
from BaseAI import BaseAI
 
class PlayerAI(BaseAI):
	
	
	def getMove(self, grid):
		moves = grid.getAvailableMoves()
		
		grid1 = self.exampleGrid(grid)
		"""print ''"""
		"""self.pretty_print(grid1)"""
		"""print ''"""
		j = self.decision(grid,4)
		"""print j.map"""
		for a in self.expandMaxDir(grid):
			if j.map == a[0].map:
				"""print a[1]"""
				defmove = a[1]
			


			
		print defmove
		raw_input("Press Enter to continue...")
		"""return moves[randint(0, len(moves) - 1)] if moves else None"""
		return 1
	
	def heuristic(self,node):
	
		"""calcular heuristica nodo"""
		node_temp = node.clone()
		maxTile = node_temp.getMaxTile()
		KmaxTile = 10
		freeCells = len(node_temp.getAvailableCells())
		KfreeCells = 0
		AvailableMoves = len(node_temp.getAvailableMoves())
		KAvailableMoves = 0
		ValuesCorners = self.valuesInCorners(node)
		KValuesCorners = 1
	
		return maxTile*KmaxTile + freeCells*KfreeCells + AvailableMoves*KAvailableMoves + KValuesCorners * ValuesCorners
	
	




	def minimaxalphabetapruning(self, node, depth, alpha, beta, maximizingPlayer):
		if depth == 0 or self.GoalState(node):
			return self.heuristic(node)
	
		if maximizingPlayer:
			for child in self.expandMax(node):
				alpha = max(alpha, self.minimaxalphabetapruning(child, depth - 1, alpha, beta, False))
				if beta <= alpha:
					break
			return alpha
	
		else:
			for child in self.expandMin(node):
				beta = min(beta, self.minimaxalphabetapruning(child, depth - 1, alpha, beta, True))
				if beta <= alpha:
					break
			return beta


	def expandMinSimple(self,node):
	
		grid_temp = []
		grid_temp_index = 0

		
		for indexColumn, column in enumerate(node.map):
			for indexRow, row in enumerate(column):
				if(node.canInsert([indexColumn,indexRow])):
					
					if indexColumn == indexRow and indexColumn <= 1:
						grid_temp.append(node.clone())
						grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)
						"""print str(indexColumn) + str(indexRow) + str(row)"""
						grid_temp_index +=1
		
		for indexColumn, column in enumerate(node.map):
			for indexRow, row in enumerate(column):
				if(node.canInsert([indexColumn,indexRow])):
					
					if indexColumn == indexRow and indexColumn > 1:
						grid_temp.append(node.clone())
						grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],4)
						"""print str(indexColumn) + str(indexRow) + str(row)"""
						grid_temp_index +=1
						
		return grid_temp
	


	def expandMin(self,node):
	
		grid_temp = []
		grid_temp_index = 0

		
		for indexColumn, column in enumerate(node.map):
			for indexRow, row in enumerate(column):
				if(node.canInsert([indexColumn,indexRow])):
					
					grid_temp.append(node.clone())
					grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)
					"""print str(indexColumn) + str(indexRow) + str(row)"""
					grid_temp_index +=1
		
		for indexColumn, column in enumerate(node.map):
			for indexRow, row in enumerate(column):
				if(node.canInsert([indexColumn,indexRow])):
					
					grid_temp.append(node.clone())
					grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],4)
					"""print str(indexColumn) + str(indexRow) + str(row)"""
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


		
	def pretty_print(self,grid):
	
		for indexColumn, column in enumerate(grid.map):
			
			print str(column[0])+' '+str(column[1])+' '+str(column[2])+' '+str(column[3])
			print


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
				"""print str(indexColumn) + str(indexRow) + str(row)"""
		
		exampleGrid_temp.insertTile([0,1],2)
		exampleGrid_temp.insertTile([0,2],4)
		return exampleGrid_temp




	"""algoritmo a aplicar en la ultima capa!!!"""		
	def minimax(node,depth,maximizingPlayer):

		if depth == 0 or GoalState(node):
			
			return heuristic(node)

		if maximizingPlayer:
			topVal = """menor valor heuristica = 0"""
			for childnode in expandMin(node):
				value = minimax(childnode,depth - 1, False)
				topVal = max(toVal,value)
		
			return topVal 
	
		else:
			topVal = """mayor valor heuristica = 100"""
			for childnode in heuristic(node):
				value = minimax(childnode, depth -1, True)
				topVal = min(topVal, value)
				
			return topVal

	"""def freeZeroColumnsRows(self,node):"""
		
	
	
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
	
		return a + b +c + d


	def abmaximize(self,node,alpha,beta, depth):
		
		if self.GoalState(node) or depth == 0:
			return ( None ,self.heuristic(node))
			
		maxUtility = -9999
		maxChild = None
			
		for child in self.expandMax(node):
			
			(_,utility) = self.abminimize(child,-9999,9999, depth - 1)
			
			if utility > maxUtility:
				(maxChild, maxUtility) = (child, utility)
				
			if maxUtility >= beta:
				break
				
			if maxUtility > alpha:
				alpha = maxUtility
		
		return (maxChild,maxUtility)





	def abminimize(self, node, alpha, beta, depth):

		
		if self.GoalState(node) or depth == 0:
			return (None,self.heuristic(node))
		
		minUtility = 9999
		minChild = None
		
		for child in self.expandMin(node):
			
			(_,utility) = self.abmaximize(child,-9999,9999, depth - 1)
			
			if utility < minUtility:
				(minChild,minUtility) = (child,utility)
			
			if minUtility <= alpha:
				break
			
			if minUtility < beta:
				beta = minUtility
			
			
		return (minChild, minUtility)


	def decision(self,node, depth):
		
		(child, _ ) = self.abmaximize(node,-9999,9999, depth)
		
		return child


	