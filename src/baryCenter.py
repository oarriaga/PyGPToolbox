## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: m-by-3 numpy ndarray of face indices
##
## Outputs:
## B: m-by-3 numpy ndarray

import numpy as np

def baryCenter(V, F):
	B = np.zeros((F.shape[0],V.shape[1]))
	for ii in range(F.shape[1]):
		B += 1.0/F.shape[1] * V[F[:,ii],:]
	return B