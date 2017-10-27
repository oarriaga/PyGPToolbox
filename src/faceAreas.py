## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: m-by-3 numpy ndarray of face indices
##
## Outputs:
## face areas: m-by-3 numpy ndarray

import numpy as np
import sys

def faceAreas(V, F):    
	vec1 = V[F[:,1],:] - V[F[:,0],:]
	vec2 = V[F[:,2],:] - V[F[:,0],:]
	FN = np.cross(vec1, vec2) / 2
	faceArea = np.sqrt(np.power(FN,2).sum(axis = 1))
	return faceArea