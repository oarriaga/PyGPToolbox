## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: m-by-3 numpy ndarray of face indices
## stepSize: step size for MCF update (need to be sufficiently small)
## numLevel: number of MCF updates to process
##
## Outputs:
## MCF results: V.shape[0]-by-V.shape[1]-by-numLevel 
##
## Reference: 
## Kazhdan et al, "Can Mean-Curvature Flow be Modified to be Non-singular?", 2012

import numpy as np
import numpy.matlib as mat
import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
from cotanLaplace import *
from vertexAreas import *
from faceAreas import *
from baryCenter import *

def conformalMeanCurvatureFlow(V,F,stepSize=0.001,numLevel=10):
	V_MCF = np.zeros((V.shape[0], V.shape[1], numLevel))
	V_MCF[:,:,0] = V
	L = cotanLaplace(V, F)
	for ii in range(numLevel-1):
		VA = vertexAreas(V_MCF[:,:,ii], F)
		M = sparse.csr_matrix(np.diag(VA))
		A = M + stepSize*L
		Vnew = np.linalg.solve(A.todense(), np.matmul(M.todense(),V_MCF[:,:,ii]))
		totalNewArea = np.sum(faceAreas(Vnew, F))
		faceAreaMat = np.expand_dims((faceAreas(Vnew, F) / totalNewArea),axis=1)
		c = np.matmul(faceAreaMat.transpose(), baryCenter(Vnew, F)) # c: 1-by-3
		Vnew = Vnew - np.tile(c, [Vnew.shape[0],1])
		Vnew = Vnew / np.sqrt(totalNewArea)
		V_MCF[:,:,ii+1] = Vnew
	return V_MCF
