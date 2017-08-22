import numpy as np
import csv

from numpy import array

from numpy import genfromtxt

matrix1 = genfromtxt('input2.csv', delimiter=',')



matrix_orig = 1 * matrix1

b1 = matrix_orig [:,0]
b2 = matrix_orig [:,1]
b3 = matrix_orig [:,2]



mean_b1 = np.mean(b1, axis=0)
mean_b2 = np.mean(b2, axis=0)
mean_b3 = np.mean(b3, axis=0)

std_b1 = np.std(b1, axis=0)
std_b2 = np.std(b2, axis=0)
std_b3 = np.std(b3, axis=0)



b1[:] = [(x - mean_b1)/std_b1 for x in b1]

b2[:] = [(x - mean_b2)/std_b2 for x in b2]

"b3[:] = [(x - mean_b3)/std_b3 for x in b3]"




matrix2 = np.column_stack((b1,b2,b3))





nsamples = len(matrix2)




matrix_n = np.c_[np.ones(nsamples), matrix2]

vector_n = matrix_n[:,3]

matrix_n = np.delete(matrix_n, 3, axis=1)


matrixT_n = matrix_n.transpose()


matrixMult_n = np.dot(matrixT_n,matrix_n)


matrixInv_n = np.linalg.inv(matrixMult_n)


matrixMult2_n = np.dot(matrixInv_n,matrixT_n)


resultado_n = np.dot(matrixMult2_n,vector_n)

print 'resultado'
print str(resultado_n)
