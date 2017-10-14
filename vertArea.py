## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: n-by-3 numpy ndarray of face indices

import numpy as np

def vertArea(V, F):
    numVert = V.shape[0]
    numFace = F.shape[0]
    
    vec1 = V[F[:,1],:] - V[F[:,0],:]
    vec2 = V[F[:,2],:] - V[F[:,0],:]
    faceNormal = np.cross(vec1, vec2) / 2
    faceArea = np.sqrt(np.power(faceNormal,2).sum(axis = 1))
    vertArea = np.zeros((numVert))
    for faceIdx in range(numFace):
        v0 = F[faceIdx, 0]
        v1 = F[faceIdx, 1]
        v2 = F[faceIdx, 2]
        vertArea[v0] += faceArea[faceIdx]/3;
        vertArea[v1] += faceArea[faceIdx]/3;
        vertArea[v2] += faceArea[faceIdx]/3;  
    return vertArea