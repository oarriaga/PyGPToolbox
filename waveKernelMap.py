## Reference:
## 1. Aubry et al, "The wave kernel signature: A quantum mechanical approach to shape analysis", 2011
## 2. http://www.lix.polytechnique.fr/~maks/fmaps_SIG17_course/publications.html

import numpy as np
import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
from cotanLaplace import *
from vertexAreas import *

def waveKernelMap(V,F, landmarks, numEigs = 300, numTimes = 200):
	WKM = []

	VA = vertexAreas(V,F)
	VAMat = sparse.csr_matrix(np.diag(VA))
	L = cotanLaplace(V,F)

	eVal, eVec = scipy.sparse.linalg.eigsh(L, M=VAMat, k=numEigs+1, which='LM', sigma = 0)
	eVal = np.delete(eVal, 0) # remove the first eVal
	eVec = np.delete(eVec, 0, axis = 1) # remove the first eVec

	emin = np.log(eVal[0])
	emax = np.log(eVal[numEigs-1])
	sigma = 7*(emax - emin) / numTimes
	emin = emin + 2*sigma
	emax = emax - 2*sigma
	eSteps = np.linspace(emin, emax, numTimes)
	eTile = np.tile(np.log(np.expand_dims(eVal, axis=1)), [1, numTimes])
	eStepsTile = np.tile(np.expand_dims(eSteps, axis=0), [numEigs, 1])
	T = np.exp(-(eTile-eStepsTile)**2/(2*sigma*sigma))
	
	for l in landmarks:
		seg = np.zeros((V.shape[0], 1))
		seg[l,0] = 1
		WKS = np.tile(np.matmul(eVec.transpose(), seg), [1, numTimes])
		WKS = np.multiply(T, WKS)
		WKS = np.matmul(eVec, WKS)
		if WKM == []:
			WKM = WKS
		else:
			WKM = np.concatenate((WKM, WKS), axis = 1)

	return WKM

