## Reference:
## 1. Botsch et al, "Polygon Mesh Processing", 2010
## 2. Meyer et al, "Discrete Differential-Geometry Operators for Triangulated 2-Manifolds", 2003

import numpy as np 
import scipy
from scipy.sparse import csr_matrix
from vertexAreas import *

def gaussianCurvature(V,F):
	# compute sum of internal angles
	idx1 = F[:,0]
	idx2 = F[:,1]
	idx3 = F[:,2]
	norm12 = np.sqrt(np.sum((V[idx2,:] - V[idx1,:])**2, axis = 1))
	norm13 = np.sqrt(np.sum((V[idx3,:] - V[idx1,:])**2, axis = 1))
	norm23 = np.sqrt(np.sum((V[idx3,:] - V[idx2,:])**2, axis = 1))
	theta23 = np.arccos((norm12**2 + norm13**2 - norm23**2) / (2 * norm12 * norm13))
	theat13 = np.arccos((norm23**2 + norm12**2 - norm13**2) / (2 * norm23 * norm12))
	theta12 = np.arccos((norm13**2 + norm23**2 - norm12**2) / (2 * norm13 * norm23))
	theta23 = np.expand_dims(theta23, axis =1)
	theat13 = np.expand_dims(theat13, axis =1)
	theta12 = np.expand_dims(theta12, axis =1)
	internalAngle = np.concatenate((theta23, theat13, theta12), axis=1)

	# compute Gaussian curvature 
	rowIdx = F.reshape((F.shape[0] * F.shape[1]))
	colIdx = np.zeros((rowIdx.shape[0]))
	data = internalAngle.reshape((F.shape[0] * F.shape[1]))
	K = 2*np.pi - csr_matrix( (data, (rowIdx, colIdx)), shape=(V.shape[0],1)).todense()
	VA = vertexAreas(V,F)
	K = np.squeeze(K) / (VA+np.finfo(float).eps)
	return K