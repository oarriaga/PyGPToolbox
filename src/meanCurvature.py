## Reference
## Botsch et al, "Polygon Mesh Processing", 2010

import numpy as np 
from cotanLaplace import *
from vertexAreas import *

def meanCurvature(V,F):
	L = cotanLaplace(V,F)
	VA = vertexAreas(V, F)
	inv_M = scipy.sparse.csr_matrix(np.diag(1/(VA+np.finfo(float).eps)))
	L = inv_M * L
	H = np.sqrt(np.sum((L*V)**2, axis=1)) / 2.0
	return H


