## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: m-by-3 numpy ndarray of face indices
##
## Outputs:
## face normals: m-by-3 numpy ndarray

import numpy as np
import sys

def faceNormals(V, F):    
	vec1 = V[F[:,1],:] - V[F[:,0],:]
	vec2 = V[F[:,2],:] - V[F[:,0],:]
	FN = np.cross(vec1, vec2) / 2
	l2Norm = np.sqrt((FN * FN).sum(axis=1))
	FN_normalized = FN / l2Norm.reshape(FN.shape[0],1)
	return FN_normalized