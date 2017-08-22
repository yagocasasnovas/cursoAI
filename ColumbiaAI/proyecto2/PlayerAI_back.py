""" test """
"""2 sale con 90% y 4 con 10%"""


from BaseAI import BaseAI
 
class PlayerAI(BaseAI):
	
	plus_infinite = 9999999
	minus_infinite = -9999999
	alphaclass = 123
	betaclass = 123
	
	
	def getMove(self, grid):


		j = self.decision(grid,4)
		
		if j is None:
			
			j = self.decision(grid,2)
			
			if j is None:
				
				j = self.decision(grid,1)

		for a in self.expandMaxDir(grid):
			if j.map == a[0].map:

				defmove = a[1]
				return defmove

