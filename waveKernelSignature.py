## Reference:
## Aubry et al, "The wave kernel signature: A quantum mechanical approach to shape analysis", 2011

import numpy as np
import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
from cotanLaplace import *
from vertexAreas import *

def waveKernelSignature(V,F, numEigs = 300, numTimes = 200):
	VA = vertexAreas(V,F)
	VAMat = sparse.csr_matrix(np.diag(VA))
	L = cotanLaplace(V,F)

	eVal, eVec = scipy.sparse.linalg.eigsh(L, M=VAMat, k=numEigs+1, which='LM', sigma = 0)
	eVal = np.delete(eVal, 0) # remove the first eVal
	eVec = np.delete(eVec, 0, axis = 1) # remove the first eVec
	D = np.matmul(eVec.transpose(), np.matmul(VAMat.todense(), eVec**2))

	emin = np.log(eVal[0])
	emax = np.log(eVal[numEigs-1])
	sigma = 7*(emax - emin) / numTimes
	emin = emin + 2*sigma
	emax = emax - 2*sigma
	eSteps = np.linspace(emin, emax, numTimes)

	eTile = np.tile(np.log(np.expand_dims(eVal, axis=1)), [1, numTimes])
	eStepsTile = np.tile(np.expand_dims(eSteps, axis=0), [numEigs, 1])

	T = np.exp(-(eTile-eStepsTile)**2/(2*sigma*sigma))
	WKS = np.matmul(eVec, np.matmul(D, T))
	return WKS




