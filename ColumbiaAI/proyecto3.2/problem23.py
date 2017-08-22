import numpy as np
import csv

from numpy import array



csv1 = np.genfromtxt ('input2.csv', delimiter=",")
age = csv1[:,0]
weight = csv1[:,1]
height = csv1[:,2]

number_samples = len(age)

age_np = array(age)
weight_np = array(weight)
height_np = array(height)


mean_age = np.mean(age_np, axis=0)
mean_weight = np.mean(weight_np, axis=0)
mean_height = np.mean(height_np, axis=0)

std_age = np.std(age_np, axis=0)
std_weight = np.std(weight_np, axis=0)
std_height = np.std(height_np, axis=0)

age_norm = []
weight_norm = []
height_norm = []

for weight_1 in weight_np:
	weight_norm.append((weight_1-mean_weight)/std_weight)

for height_1 in height_np:
	height_norm.append((height_1-mean_height)/std_height)

for age_1 in age_np:
	age_norm.append((age_1-mean_age)/std_age)
	

intercept = [1] * number_samples

data_matrix = zip(intercept, age_norm, weight_norm, height_norm)




learning_rates = [0.5]



def risk_function(data_matrix_in,betas_in):
	
	suma_parcial = 0
	
	for a in range(number_samples):
		
		func = betas_in[0] + betas_in[1]*data_matrix_in[a][1] + betas_in[2]*data_matrix_in[a][2]
		
		squared = (data_matrix_in[a][3]-func)*(data_matrix_in[a][3]-func)
		
		suma_parcial = suma_parcial + squared
		
	return suma_parcial / (2*number_samples)
	
	
	
"""print risk_function(data_matrix,betas)"""



"lr = learning_rates[5]"
"lr = 0.91"

for idx, lr in enumerate(learning_rates):
	
	betas = [0,0,0]
	iterations = 100
	riesgo = 9999999999

	for it in range(iterations):
	
		suma_parcial0 = 0
		suma_parcial1 = 0
		suma_parcial2 = 0
	
		for a in range(number_samples):
		
			suma_parcial0 = suma_parcial0 + betas[0] + betas[1]*data_matrix[a][1] + betas[2]*data_matrix[a][2] - data_matrix[a][3]
			suma_parcial1 = suma_parcial1 + (betas[0] + betas[1]*data_matrix[a][1] + betas[2]*data_matrix[a][2] - data_matrix[a][3])*data_matrix[a][1]
			suma_parcial2 = suma_parcial2 + (betas[0] + betas[1]*data_matrix[a][1] + betas[2]*data_matrix[a][2] - data_matrix[a][3])*data_matrix[a][2]
	
	
	
		betas[0] = betas[0] - (lr/number_samples) * suma_parcial0
		betas[1] = betas[1] - (lr/number_samples) * suma_parcial1
		betas[2] = betas[2] - (lr/number_samples) * suma_parcial2
	
	
		riesgo_parcial = risk_function(data_matrix,betas)
		print str(it) + ' '  + str(riesgo) + ' ' + str(riesgo_parcial) + str(riesgo - riesgo_parcial)
		if riesgo_parcial < riesgo:
			riesgo = riesgo_parcial
		else:
			break
	
	print str(lr) + ' ' + str(it) + ' ' + str(betas[0]) + ' ' + str(betas[1])+ ' ' + str(betas[2]) + ' ' + str(riesgo)
	
	
	
	
	
	