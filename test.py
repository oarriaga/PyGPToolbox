from readOBJ import *
from vertArea import *
from cotanLaplace import *
from adjacencyMat import *
from plotTriMesh import *
from KNearestNeighborsSearch import *
#from mayavi import mlab
import scipy
import scipy.spatial
import scipy.sparse
import scipy.sparse.linalg

V,F = readOBJ('./meshes/spot.obj')
VA = vertArea(V, F)
L = cotanLaplace(V,F)
A = adjacencyMat(F)

massMat = scipy.sparse.coo_matrix(np.diag(VA)).tocsr()
vals, vecs = scipy.sparse.linalg.eigsh(L, M=massMat, k=5, which='LM', sigma=0)

# plotTriMesh(V,F, vertexColor = vecs[:,0])
dist, NNIdx = KNearestNeighborsSearch(vecs, vecs, 1)
print dist
print NNIdx