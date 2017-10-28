# compute edges from faces

import numpy as np

def edges(F):
	idx = np.array([[0,1], [1,2], [2,0]])
	edgeIdx1 = np.reshape(F[:,idx[:,0:1]], (np.product(F.shape),1))
	edgeIdx2 = np.reshape(F[:,idx[:,1:2]], (np.product(F.shape),1))
	edge = np.concatenate((edgeIdx1, edgeIdx2), axis =1)
	edge = np.sort(edge, axis = 1)
	edge = np.unique(edge, axis = 0)
	return edge