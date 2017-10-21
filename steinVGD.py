## Stein Variational Gradient Descent
## Reference: Liu et al, "Stein Variational Gradient Descent (SVGD): A General Purpose Bayesian Inference Algorithm", NIPS 2016
## This code is modified from: https://github.com/DartML/Stein-Variational-Gradient-Descent

import numpy as np
import numpy.matlib as mat
from scipy.spatial.distance import pdist, squareform

def kernelRBF(x):
	dist = pdist(x)
	distMat = squareform(dist)
	med = np.median(distMat)
	h = med**2 / np.log(x.shape[0]+1)
	RBF = np.exp(-1/h * np.power(distMat,2))

	dRBF_dx = -np.matmul(RBF, x)
	sumRBF = np.expand_dims(np.sum(RBF, axis = 1), axis = 1)
	dRBF_dx += x * mat.repmat(sumRBF, 1, x.shape[1])
	dRBF_dx = dRBF_dx / (0.5*h)
	return RBF, dRBF_dx

def steinVGD(x0, dlogp_dx_func, numIter = 1000, stepSize = 1e-2):
	x = x0
	for eqoch in range(numIter):
		dlogpdx = dlogp_dx_func(x)
		RBF, dRBF_dx = kernelRBF(x)
		gradX = (np.matmul(RBF, dlogpdx) + dRBF_dx) / x.shape[0]
		x = x + stepSize * gradX
	return x 