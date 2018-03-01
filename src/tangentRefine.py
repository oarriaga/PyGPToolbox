from allVertexOneRings import *
from vertexNormals import *
import itertools
import numpy as np

def tangentRefine(V,F, numIter = 15):
	VHis = V[:,:,None]

	# compute one rings
	oneRings = allVertexOneRings(V,F)
	numNeighbors = np.array([len(x) for x in oneRings])
	np_oneRings = np.array(list(itertools.izip_longest(*oneRings, fillvalue=V.shape[0]))).T

	for iter in range(numIter):
		# compute avg of each one ring
		temp_V = np.concatenate((VHis[:,:,iter], np.array([[0,0,0]])), axis =0)
		avgCenter = np.sum(temp_V[np_oneRings, :], axis = 1) / numNeighbors[:,None]
		# disp vector 
		dispVec = avgCenter - VHis[:,:,iter]
		# remove normal part
		VN = vertexNormals(VHis[:,:,iter],F)
		newV = VHis[:,:,iter] + dispVec - np.sum(dispVec * VN, axis = 1)[:,None] *VN

		# add to history
		VHis = np.concatenate((VHis, newV[:,:,None]), axis = 2)
	return VHis[:,:,-1], VHis