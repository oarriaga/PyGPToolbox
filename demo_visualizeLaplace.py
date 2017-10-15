import scipy
import scipy.sparse
import scipy.sparse.linalg

from readOBJ import *
from vertArea import *
from cotanLaplace import *
from plotTriMesh import *

V,F = readOBJ('./meshes/spot.obj')
VA = vertArea(V, F)
L = cotanLaplace(V,F)

massMat = scipy.sparse.coo_matrix(np.diag(VA)).tocsr()
vals, vecs = scipy.sparse.linalg.eigsh(L, M=massMat, k=5, which='SM')

plotTriMesh(V,F, vertexColor = vecs[:,1]) 