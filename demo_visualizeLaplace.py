import scipy
import scipy.sparse
import scipy.sparse.linalg
from mayavi import mlab

from readOBJ import *
from vertexAreas import *
from cotanLaplace import *
from plotTriMesh import *

V,F = readOBJ('./meshes/spot.obj')
VA = vertexAreas(V, F)
L = cotanLaplace(V,F)

numEigs = 10
massMat = scipy.sparse.csr_matrix(np.diag(VA))
# note that: computing which='SM' directly is too slow. We use "shift-invert" to compute
eVal, eVec = scipy.sparse.linalg.eigsh(L, M=massMat, k=numEigs, which='LM', sigma = 0)

# make animation
@mlab.show
@mlab.animate(delay=600, ui=True)
def anim():
	ii = 1
	while True:
	    plotTriMesh(V,F, vertexColor = eVec[:,ii])
	    ii += 1
	    if ii == numEigs:
	    	break
	    yield
anim()