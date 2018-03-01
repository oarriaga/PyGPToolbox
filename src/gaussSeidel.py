# Gauss-Seidel iterative solver
import numpy as np

def gaussSeidel(A, b, initX = -1, maxIter = 100):
	# A is n-by-n np array
	# b is 1-dim np array with size n
	# initX is 1-dim np array with size n (initial guess)
	D = np.diag(np.diag(A))
	U = np.triu(A) - D
	L = np.tril(A) - D

	# initialize x
	if initX.all() != -1:
		x = np.copy(initX)
	else:
		x = np.zeros(b.shape)

	# GS iteration
	for ii in range(maxIter):
		error = np.linalg.norm(A.dot(x) - b)
		x = np.linalg.inv(D+L).dot(-U.dot(x) + b) 
		if np.linalg.norm(A.dot(x) - b) == error: # is converge
			print "iteration:", ii
			break
	return x

# simple test
# A = np.array([[2, 1], [5,7]])
# b = np.array([11, 13])
# initX = np.array([1, 1])
# x = gaussSeidel(A, b, initX)
# print "solution:", x
# print "error:", np.linalg.norm(A.dot(x) - b)