import numpy as np
import csv



csv1 = np.genfromtxt ('input1.csv', delimiter=",")
first = csv1[:,0]
second = csv1[:,1]
third = csv1[:,2]


fourth = zip(first, second, third)




"number of iterations"
k = 100

weights = [0,0,0]

def sign_function(w,x,y):
	
	if w[2] + w[0]*x + w[1]*y > 0:
		return 1
	else:
		return -1



for a in range(k):

	total_error = 0
	
	for xx in fourth:
		
		output = sign_function(weights,xx[0],xx[1])
		error = xx[2] - output
		
		total_error = total_error + error
		
		if xx[2]*output < 0:
			
			weights[2] = weights[2] + error
			weights[0] = weights[0] + error * xx[0]
			weights[1] = weights[1] + error * xx[1]
			
		"""print str(weights) + str(total_error)"""
		
	if total_error == 0:
		break;


	with open('output1.csv','a') as f:
		

		writer1 = csv.writer(f)
		writer1.writerow(weights)
		
	