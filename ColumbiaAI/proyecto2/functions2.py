	def pretty_print(self,grid):
	
		for indexColumn, column in enumerate(grid.map):
			
			"""print str(column[0])+' '+str(column[1])+' '+str(column[2])+' '+str(column[3])"""
			break
			
			
				def expandMinSimple(self,node):
	
		grid_temp = []
		grid_temp_index = 0

		
		for indexColumn, column in enumerate(node.map):
			for indexRow, row in enumerate(column):
				if(node.canInsert([indexColumn,indexRow])):
					
					if indexColumn == indexRow and indexColumn <= 1:
						grid_temp.append(node.clone())
						grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],2)

						grid_temp_index +=1
		
		for indexColumn, column in enumerate(node.map):
			for indexRow, row in enumerate(column):
				if(node.canInsert([indexColumn,indexRow])):
					
					if indexColumn == indexRow and indexColumn > 1:
						grid_temp.append(node.clone())
						grid_temp[grid_temp_index].insertTile([indexColumn,indexRow],4)

						grid_temp_index +=1
						
		return grid_temp
		
		
		
		


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