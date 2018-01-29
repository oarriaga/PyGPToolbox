import numpy as np

def extractBoundaryVertices(V,F):
	idx = np.array([[0,1], [1,2], [2,0]])
	EIdx1 = np.reshape(F[:,idx[:,0:1]], (np.product(F.shape),1))
	EIdx2 = np.reshape(F[:,idx[:,1:2]], (np.product(F.shape),1))
	EAll = np.concatenate((EIdx1, EIdx2), axis =1)
	EAll = np.sort(EAll, axis = 1)
	E, counts = np.unique(EAll, axis = 0, return_counts = True)
	idx = np.where(counts == 1)[0]
	bdVIdx = np.unique(E[idx,:].flatten())
	return bdVIdx