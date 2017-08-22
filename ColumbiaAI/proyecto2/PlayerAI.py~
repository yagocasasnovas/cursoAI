""" test """
"""2 sale con 90% y 4 con 10%"""


from BaseAI import BaseAI

from mainfunctions import decision
from auxfunctions import exampleGrid3, pretty_print

from heuristicfunctions import cleardict

import time
 
class PlayerAI(BaseAI):
	
	"""grid artificial para pruebas"""
	
	
	
	def getMove(self, grid):

		"""a = decision(grid,4)"""
		
#		grid3 = exampleGrid3(grid)
#		print "hola"
#		pretty_print(grid3)
		
		cleardict()
		
		t = time.clock()
#		((a,b),c) = decision(grid3,t)
		c = decision(grid,t)
		"""print("--- %s seconds ---" % (time.clock() - t))"""
		"""print"""
		"""print "explored: " + str(a)"""
		"""print "pruned: " + str(b)"""
		
		
	
		
		return c