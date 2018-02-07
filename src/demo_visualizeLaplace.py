import scipy
import scipy.sparse
import scipy.sparse.linalg
# from mayavi import mlab

from readOBJ import *
from vertexAreas import *
from cotanLaplace import *
# from animateVertexColor import *
from meshColorAnimation import *

V,F = readOBJ('../meshes/tr_reg_089.obj')
VA = vertexAreas(V, F)
L = cotanLaplace(V,F)

numEigs = 20
massMat = scipy.sparse.csr_matrix(np.diag(VA))
# note that: computing which='SM' directly is too slow. We use "shift-invert" to compute
eVal, eVec = scipy.sparse.linalg.eigsh(L, M=massMat, k=numEigs, which='LM', sigma = 0)

meshColorAnimation(V,F,eVec[:,1:],colormap = 'default')

# ==============
# RIP
# ==============
# plot eigenvector
# delayTime = 500
# animateVertexColor(V,F,eVec[:,1:], delayTime, colormap="RdBu")