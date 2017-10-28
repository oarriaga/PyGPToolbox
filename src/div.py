## Reference:
## https://github.com/alecjacobson/gptoolbox/blob/master/mesh/div.m

import numpy as np 
import scipy
import scipy.sparse
from grad import *
from faceAreas import *

def div(V,F):
	G = grad(V,F)
	FA = faceAreas(V,F)
	temp = scipy.sparse.csr_matrix(np.diag(np.tile(FA,3)))
	D = -0.5 * G.transpose() * temp
	return D

