## Reference:
## 1. Sun et al, "A Concise and Provably Informative Multi-Scale Signature Based on Heat Diffusion" 2009
## 2. Bronstein et al, "Scale-invariant heat kernel signatures for non-rigid shape recognition", 2010
##
## to do:
## 1. make it scale invariant

import numpy as np
import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
from vertexAreas import *
from cotanLaplace import *

def heatKernelSignature(V,F, numEigs = 300, logtmax = 4, logtmin = -2, numTimeSteps = 100):
	# construct matrices
	VA = vertexAreas(V,F)
	Mv = sparse.csr_matrix(np.diag(VA))
	L = cotanLaplace(V,F)

	# solve eigenvalues and eigenvectors
	numEigs = 300
	eVal, eVec = scipy.sparse.linalg.eigsh(L, M=Mv, k=numEigs, which='LM', sigma = 0)
	eVal = np.delete(eVal, 0) # remove the first eVal
	eVec = np.delete(eVec, 0, axis = 1) # remove the first eVec

	# create time step
	logtmax = 4
	logtmin = -2
	numTimeSteps = 100
	timeSteps = np.logspace(logtmin, logtmax, num=numTimeSteps)

	# compute heat kernel signature
	temp = np.matmul(np.expand_dims(eVal, axis=1), np.expand_dims(timeSteps, axis=0))
	HKS = np.matmul(eVec**2, np.exp(-temp)) # original HKS (not scale invariant) 

	return HKS