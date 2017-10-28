## Reference:
## 1. https://github.com/alecjacobson/gptoolbox/blob/master/mesh/grad.m

import numpy as np 
import scipy
from scipy.sparse import csr_matrix
from faceNormals import *
from faceAreas import *

def grad(V,F):
	i1 = F[:,0]
	i2 = F[:,1]
	i3 = F[:,2]
	V13 = V[i1,:] - V[i3,:]
	V21 = V[i2,:] - V[i1,:]
	V32 = V[i3,:] - V[i2,:]
	FN = faceNormals(V,F)
	FA = np.expand_dims(faceAreas(V,F), axis = 1)
	eperp21 = np.cross(FN, V21) / (2*np.tile(FA, [1,3]))
	eperp13 = np.cross(FN, V13) / (2*np.tile(FA, [1,3]))

	nF = F.shape[0] # number of faces
	temp1 = 0*nF + np.tile(range(nF), 4)
	temp2 = 1*nF + np.tile(range(nF), 4)
	temp3 = 2*nF + np.tile(range(nF), 4)
	rowIdx = np.concatenate((temp1, temp2, temp3), axis=0)

	temp = np.concatenate((F[:,1], F[:,0], F[:,2], F[:,0]), axis = 0)
	colIdx = np.tile(temp, 3)

	data = np.concatenate((eperp13[:,0], -eperp13[:,0], 
		eperp21[:,0], -eperp21[:,0],
		eperp13[:,1], -eperp13[:,1],
		eperp21[:,1], -eperp21[:,1],
		eperp13[:,2], -eperp13[:,2], 
		eperp21[:,2], -eperp21[:,2],), axis = 0)

	gradMat = csr_matrix( (data, (rowIdx, colIdx)),
		shape = (3*F.shape[0], V.shape[0]))
	return gradMat
