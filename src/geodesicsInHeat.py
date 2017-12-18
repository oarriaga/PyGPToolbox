## Reference:
## Crane et al, "Geodesics in Heat: A New Approach to Computing Distance Based on Heat Flow" 2013

import numpy as np
from edges import *
from cotanLaplace import *
from vertexAreas import *
from grad import *
from div import *

def geodesicsInHeat(V,F, centerIdx, m = 1.0):
	# compute fixed time step (t = mh^2)
	E = edges(F)
	edgeLength = np.sqrt(np.sum((V[E[:,0],:] - V[E[:,1],:])**2, axis =1))
	t = m*np.mean(edgeLength)**2

	## Algorithm
	# 1. solve heat diffusion
	L = cotanLaplace(V,F)
	VA = vertexAreas(V, F)
	Mv = scipy.sparse.csr_matrix(np.diag(VA))
	u0 = np.zeros((V.shape[0], 1))
	u0[centerIdx, 0] = 1 # initial heat source
	LHS = Mv + t*L
	u = np.linalg.solve(LHS.todense(), u0)

	# 2. normalize gradient
	G = grad(V,F)
	gradu = (G*u).reshape((F.shape[0], V.shape[1]))
	gradu_norm = np.sqrt(np.sum(gradu**2, axis = 1)) + np.finfo(float).eps
	gradu_normalized = gradu / np.tile(np.expand_dims(gradu_norm, axis =1), [1,3])
	X = -gradu_normalized # reverse direction

	# 3. solve poisson
	D = div(V,F)
	divX = np.matmul(D.todense(), X.reshape((F.shape[0]*3, 1)))
	phi = np.linalg.solve(L.todense(), divX)

	phi = -(phi-phi[centerIdx])
	return phi


