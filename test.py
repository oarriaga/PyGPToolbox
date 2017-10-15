from readOBJ import *
from vertArea import *
from cotanLaplace import *
from adjacencyMat import *
from plotTriMesh import *
#from mayavi import mlab
import scipy
import scipy.sparse
import scipy.sparse.linalg

V,F = readOBJ('./meshes/spot.obj')
VA = vertArea(V, F)
L = cotanLaplace(V,F)
A = adjacencyMat(F)

massMat = scipy.sparse.coo_matrix(np.diag(VA)).tocsr()
vals, vecs = scipy.sparse.linalg.eigs(L, M=massMat, k=10, which='SM')
vals = np.real(vals)
vecs = np.real(vecs)

plotTriMesh(V,F, vertexColor = vecs[:,0])
plotTriMesh(V,F, vertexColor = vecs[:,1])
plotTriMesh(V,F, vertexColor = vecs[:,2])