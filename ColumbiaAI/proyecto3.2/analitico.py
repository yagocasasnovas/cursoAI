import numpy as np
import csv

from numpy import array

from numpy import genfromtxt

matrix1 = genfromtxt('input2.csv', delimiter=',')

nsamples = len(matrix1)


matrix = np.c_[np.ones(nsamples), matrix1]

vector = matrix[:,3]

matrix = np.delete(matrix, 3, axis=1)


matrixT = matrix.transpose()

matrixMult = np.dot(matrixT,matrix)


matrixInv = np.linalg.inv(matrixMult)

matrixMult2 = np.dot(matrixInv,matrixT)

resultado = np.dot(matrixMult2,vector)


print 'resultado'
print resultado
