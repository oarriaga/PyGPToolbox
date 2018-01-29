# implementation of [Kobbelt. "sqrt(3)-subdivision." 2000]

import numpy as np
import scipy
import scipy.sparse as sparse

from edges import *
from adjacencyMat import *

def sqrt3Subdivision(V,F):
	E = edges(F)

	nF = F.shape[0]
	nV = V.shape[0]
	nE = E.shape[0]

	# construct e2f
	i = np.concatenate((F[:,0], F[:,1], F[:,2]))
	j = np.concatenate((F[:,1], F[:,2], F[:,0]))
	s = np.concatenate((range(nF),range(nF),range(nF)))
	e2f = sparse.csr_matrix((s, (i, j)), shape=(nV, nV))

	# compute 
	Vout = (V[F[:,0],:] + V[F[:,1],:] + V[F[:,2],:]) / 3
	Vout = np.concatenate((V, Vout), axis = 0)

	Fout = []
	for i in range(nE):
		v1 = E[i,0]
		v2 = E[i,1]
		F1 = e2f[v1, v2]
		F2 = e2f[v2, v1]
		Fout.append(np.array([v1, nV+F1, nV+F2]))
		Fout.append(np.array([v2, nV+F2, nV+F1]))
	Fout = np.array(Fout)

	# make the orientation correct
	temp = np.copy(Fout[:, 1])
	Fout[:, 1] = Fout[:, 2]
	Fout[:, 2] = temp

	# compute vertex one ring
	A = adjacencyMat(F)
	i,j,s = sparse.find(A)
	Vring = {}
	for ii in range(len(i)):
		Vring.setdefault(i[ii],[]).append(j[ii])

	# move old vertices
	for k in range(nV):
		m = len(Vring[k])
		beta = (4-2*np.cos(2*np.pi/m)) / (9*m)
		Vout[k,:] = V[k,:] * (1-m*beta) + beta*np.sum(V[Vring[k], :], axis =0)

	return Vout, Fout