import scipy
import scipy.sparse
import scipy.sparse.linalg
import time

from readOBJ import *
from vertArea import *
from cotanLaplace import *
from plotTriMesh import *

V,F = readOBJ('./meshes/spot.obj')
VA = vertArea(V, F)
L = cotanLaplace(V,F)

numEigs = 10
massMat = scipy.sparse.csr_matrix(np.diag(VA))
# note that: computing which='SM' directly is too slow. We use "shift-invert" to compute
vals, vecs = scipy.sparse.linalg.eigsh(L, M=massMat, k=numEigs, which='LM', sigma = 0)

# print vals
plotTriMesh(V,F, vertexColor = vecs[:,1]) 