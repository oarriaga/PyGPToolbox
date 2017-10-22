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
## Desbrun et al, "Implicit fairing of irregular meshes using diffusion and curvature flow", 1999
##
## Notes:
## This MCF is not robust when surface have singularity

import numpy as np
import numpy.matlib as mat
import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
from cotanLaplace import *
from vertexAreas import *

def implicitMeanCurvatureFlow(V,F,stepSize=0.001,numLevel=10):
	V_MCF = np.zeros((V.shape[0], V.shape[1], numLevel))
	V_MCF[:,:,0] = V
	for ii in range(numLevel-1):
		L = cotanLaplace(V_MCF[:,:,ii], F)
		VA = vertexAreas(V_MCF[:,:,ii], F)
		M_inv = sparse.csr_matrix(np.diag(1/(VA+np.finfo(float).eps)))
		L = M_inv * L
		A = stepSize*L + sparse.eye(V.shape[0])
		V_MCF[:,:,ii+1] = np.linalg.solve(A.todense(), V_MCF[:,:,ii])
	return V_MCF





