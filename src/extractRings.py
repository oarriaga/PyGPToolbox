import numpy as np
from find import *

def extractRings(V,F,centerVIdx,numRings = 1):
	VIdx = centerVIdx
	for ii in range(numRings):
		r,c = find(F,VIdx)
		VIdx = np.unique(F[r,:])
	return VIdx