import numpy as np

def find(F, VIdx):
	# return the indices of VIdx in F
	mask = np.in1d(F.flatten(),VIdx)
	r = np.floor(np.where(mask)[0] / 3.0).astype(int)
	c = np.where(mask)[0] % 3
	return r,c