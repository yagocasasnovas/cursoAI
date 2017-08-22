import numpy as np
import csv

from numpy import array
from matplotlib import pyplot

import pylab
from mpl_toolkits.mplot3d import Axes3D




csv1 = np.genfromtxt ('input2.csv', delimiter=",")
age = csv1[:,0]
weight = csv1[:,1]
height = csv1[:,2]

number_samples = len(age)



min_age = min(age)
max_age = max(age)

min_weight = min(weight)
max_weight = max(weight)




learning_rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 0.9763]

learning_rates = [0.004]


def risk_function(age_in, weight_in, height_in,betas_in, number_samples_in):
	
	suma_parcial = 0
	
	for a in range(number_samples_in):
		
		func = betas_in[0] + betas_in[1]*age_in[a] + betas_in[2]*weight_in[a]
				
		squared = (height_in[a]-func)*(height_in[a]-func)
		
		suma_parcial = suma_parcial + squared
		
	return suma_parcial / (2*number_samples_in)
	
	




pyplot.ion()

xx, yy = np.meshgrid(range(int(round(min_age))-1,int(round(max_age))), range(int(round(min_weight))-1,int(round(max_weight))))
fig = pyplot.figure()
ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')


for idx, lr in enumerate(learning_rates):
	
	betas = [0,0,0]
	iterations = 10000
	riesgo = 9999

	for it in range(iterations):
	
		suma_parcial0 = 0
		suma_parcial1 = 0
		suma_parcial2 = 0
		
		
		for a in range(number_samples):
		
			suma_parcial0 = suma_parcial0 + betas[0] + betas[1]*age[a] + betas[2]*weight[a] - height[a]
			suma_parcial1 = suma_parcial1 + (betas[0] + betas[1]*age[a] + betas[2]*weight[a] - height[a])*age[a]
			suma_parcial2 = suma_parcial2 + (betas[0] + betas[1]*age[a] + betas[2]*weight[a] - height[a])*weight[a]
	
	
	
		betas[0] = betas[0] - (lr/number_samples) * suma_parcial0
		betas[1] = betas[1] - (lr/number_samples) * suma_parcial1
		betas[2] = betas[2] - (lr/number_samples) * suma_parcial2
	
	
		riesgo_parcial = risk_function(age, weight, height, betas, number_samples)
		
		print str(lr) + ' ' + str(it) + ' ' + str(betas[0]) + ' ' + str(betas[1])+ ' ' + str(betas[2]) + ' ' + str(riesgo)
		
		if riesgo_parcial <= riesgo:
			riesgo = riesgo_parcial
		else:
			"break"
		
		
		z = betas[1]*xx + betas[2]*yy + betas[0]
		ax.cla()
		ax.scatter(age, weight, height)
		"""ax.plot_surface(xx, yy, z, rstride=1, cstride=1, alpha=0.2)"""
		ax.plot_surface(xx, yy, z)
		pyplot.xlabel('age', fontsize=16)
		pyplot.ylabel('weight', fontsize=16)
		"pyplot.show()"
		
		"pyplot.pause(0.1)"
		
		

	
	"""string_result = str(lr) + ',' + str(it) + ',' + str(betas[0]) + ',' + str(betas[1])+ ',' + str(betas[2])"""
	"""string_result = [lr,it,betas[0],betas[1],betas[2]]"""
	

	
	
	