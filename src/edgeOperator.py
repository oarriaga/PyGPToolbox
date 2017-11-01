## Reference:
## He et al, "Mesh Denoising via L0 Minimization", 2013
## 
## Inputs:
## V: |V|-by-3 numpy ndarray of vertex positions
## F: |F|-by-3 numpy ndarray of face indices
##
## Outputs:
## De: |E|-by-|V| edge operator
## p1234Idx: |E|-by-4 corresponds to p1,p2,p3,p4 for each edge

import numpy as np
import numpy.linalg as LA
import scipy
import scipy.sparse as sparse

from faceAreas import *
from edges import *

def edgeOperator(V,F):
	FA = faceAreas(V,F)

	# compute edge information
	idx = np.array([[0,1], [1,2], [2,0]])
	edgeIdx1 = np.reshape(F[:,idx[:,0:1]], (np.product(F.shape),1))
	edgeIdx2 = np.reshape(F[:,idx[:,1:2]], (np.product(F.shape),1))
	edge = np.concatenate((edgeIdx1, edgeIdx2), axis =1)
	edge = np.sort(edge, axis = 1)
	edgeAdjFaces = np.tile(np.expand_dims(range(F.shape[0]), axis = 1), [1, 3])
	edgeAdjFaces = edgeAdjFaces.reshape((edgeAdjFaces.shape[0] * edgeAdjFaces.shape[1]))
	E = np.unique(edge, axis = 0)

	# create unique 1d edge list
	nF = F.shape[0]
	mulNum = np.power(10, (len(str(nF))))
	uniqueID = edge[:,0] * mulNum + edge[:,1]

	def returnEdgeAdjFaceIdx(anEdge, mulNum = mulNum, edgeAdjFaces = edgeAdjFaces, uniqueID = uniqueID):
		# a function which returns adjacent face indices of an edge
		ID = anEdge[0] * mulNum + anEdge[1]
		rowIdx = np.where(uniqueID == ID)[0]
		adjFaceIdx = edgeAdjFaces[rowIdx]
		return adjFaceIdx

	De = sparse.lil_matrix((E.shape[0], V.shape[0]))
	p1234Idx = np.zeros((E.shape[0], 4))
	for ii in xrange(E.shape[0]):
		p1Idx = E[ii,0]
		p3Idx = E[ii,1]
		adjFIdx = returnEdgeAdjFaceIdx(E[ii,:])
		tempF = F[adjFIdx[0],:]
		idx1 = np.argwhere(tempF == p1Idx)[0,0]
		idx3 = np.argwhere(tempF == p3Idx)[0,0]
		if np.mod(idx3-idx1+3, 3) == 1: # right triangle
			p4Idx = tempF[np.mod(idx3+1, 3)]
			tempF = F[adjFIdx[1],:]
			idx1 = np.argwhere(tempF == p1Idx)[0,0]
			p2Idx = tempF[np.mod(idx1+1, 3)]
			leftFIdx = adjFIdx[0]
			rightFIdx = adjFIdx[1]
		else: # left triangle
			p2Idx = tempF[np.mod(idx1+1, 3)]
			tempF = F[adjFIdx[1],:]
			idx3 = np.argwhere(tempF == p3Idx)[0,0]
			p4Idx = tempF[np.mod(idx3+1, 3)]
			leftFIdx = adjFIdx[1]
			rightFIdx = adjFIdx[0]
		# print E[ii,:]
		# print p1Idx, p2Idx, p3Idx, p4Idx
		# print F[leftFIdx]
		# print F[rightFIdx]

		A123 = FA[leftFIdx]
		A134 = FA[rightFIdx]
		p1 = V[p1Idx,:]
		p2 = V[p2Idx,:]
		p3 = V[p3Idx,:]
		p4 = V[p4Idx,:]

		p1234Idx[ii,:] = np.array([p1Idx, p2Idx, p3Idx, p4Idx])
		De[ii, p1Idx] = (A123*np.dot(p4-p3, p3-p1) + A134*np.dot(p1-p3, p3-p2)) / (LA.norm(p3-p1)**2*(A123+A134))
		De[ii, p2Idx] = A134 / (A123 + A134)
		De[ii, p3Idx] = (A123*np.dot(p3-p1, p1-p4) + A134*np.dot(p2-p1, p1-p3)) / (LA.norm(p3-p1)**2*(A123+A134))
		De[ii, p4Idx] = A123 / (A123 + A134)
	return De, p1234Idx.astype(int)

