## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: m-by-3 numpy ndarray of face indices
##
## Outputs:
## A: m-by-m signed dihedral angle matrix between adjacent faces
##
## Notes:
## A[i,j] --> 0   for convex 
## A[i,j] --> pi  for flat
## A[i,j] --> 2pi for concave

import numpy as np
import scipy
import scipy.sparse as sparse
from faceNormals import *

def dihedralAngleMat(V,F):
	idx = np.array([[0,1], [1,2], [2,0]])
	EIdx1 = np.reshape(F[:,idx[:,0:1]], (np.product(F.shape),1))
	EIdx2 = np.reshape(F[:,idx[:,1:2]], (np.product(F.shape),1))
	EAll = np.concatenate((EIdx1, EIdx2), axis =1)

	temp = np.sort(EAll, axis = 1)
	mulNum = np.power(10, (len(str(F.shape[0]))))
	uniqueEID = temp[:,0] * mulNum + temp[:,1]
	sortEIdx = np.argsort(uniqueEID)
	EAll = EAll[sortEIdx,:] # sort the EAll from small to large (columwise)

	EAllFaces = np.tile(np.expand_dims(range(F.shape[0]), axis = 1), [1, 3]) 
	EAllFaces = EAllFaces.reshape((EAllFaces.shape[0] * EAllFaces.shape[1])) # face index correspond to each edge in edgeAll
	EAllFaces = EAllFaces[sortEIdx]

	EAll2E = np.where(np.sort(EAll, axis = 1)[:,0] == EAll[:,0])[0]
	revEAll2E = np.where(np.sort(EAll, axis = 1)[:,0] != EAll[:,0])[0]
	E = EAll[EAll2E,:]

	adjFList = np.concatenate((np.expand_dims(EAllFaces[EAll2E], axis=1), np.expand_dims(EAllFaces[revEAll2E], axis=1)),axis =1)
	FN = faceNormals(V,F)
	EVec = V[E[:,0],:] - V[E[:,1],:]

	# compute dihedral angles
	leftFN = FN[adjFList[:,0], :]
	rightFN = FN[adjFList[:,1], :]
	unsignedDihedral = np.arccos(np.sum(leftFN * rightFN, axis = 1))

	# determine signs
	temp = np.cross(leftFN, rightFN)
	temp = np.sum(temp * EVec, axis =1)
	sign = np.sign(temp)

	signedDihedral = sign * unsignedDihedral
	signedDihedral = signedDihedral + np.pi # shift

	A = sparse.csr_matrix((signedDihedral, (adjFList[:,0], adjFList[:,1])), shape=(F.shape[0], F.shape[0]))
	A = A.maximum(A.transpose())
	return A




