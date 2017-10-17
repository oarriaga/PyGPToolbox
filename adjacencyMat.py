## Inputs:
## F: m-by-3 numpy ndarray of face indices

import numpy as np
import scipy
import scipy.sparse as sparse

def adjacencyMat(F):
    e_idx = np.array([[0,1], [1,2], [2,0]]) # assume we have simplex with DOF=3
    idx1 = np.reshape(F[:,e_idx[:,0]], (np.product(F.shape)))
    idx2 = np.reshape(F[:,e_idx[:,1]], (np.product(F.shape)))
    A = np.zeros((np.product(F.shape), np.product(F.shape)))
    A[idx1, idx2] = 1
    A[idx2, idx1] = 1
    A = sparse.csr_matrix(A)
    return A