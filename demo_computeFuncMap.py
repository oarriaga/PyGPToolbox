## Demo of functional maps
## Reference: Ovsjanikov, "Computing and Processing Correspondences with Functional Mpas", SIGGRAPH 2017

from readOBJ import *
from cotanLaplace import *
from vertexAreas import *
from KNearestNeighborsSearch import *
import scipy
import scipy.sparse
import scipy.sparse.linalg
import matplotlib.pyplot as plt 

V1,F1 = readOBJ('./meshes/tr_reg_089.obj')
V2,F2 = readOBJ('./meshes/tr_reg_090.obj')

# compute laplace eigenbases
numEigs = 100

VA = vertexAreas(V1, F1)
L = cotanLaplace(V1,F1)
massMat_1 = scipy.sparse.csr_matrix(np.diag(VA))
eVal_1, eVec_1 = scipy.sparse.linalg.eigsh(L, M=massMat_1, k=numEigs, which='LM',sigma = 0)

VA = vertexAreas(V2, F2)
L = cotanLaplace(V2,F2)
massMat_2 = scipy.sparse.csr_matrix(np.diag(VA))
eVal_2, eVec_2 = scipy.sparse.linalg.eigsh(L, M=massMat_2, k=numEigs, which='LM', sigma = 0)

# ground truth point to point map
# (in this case, p2p map is an identity matrix)
P = scipy.sparse.eye(V1.shape[0])

# visualize the functional map given p2p map
## C = eVec_2' * massMat_2' * P' * eVec_1
C = scipy.sparse.csr_matrix(eVec_2.transpose()) * massMat_2.transpose() * P.transpose() * scipy.sparse.csr_matrix(eVec_1);
C = C.todense()

# plot functional maps
plt.figure()
plt.imshow(C)
plt.title('Functional map')

# Recover p2p map given functional map C:
# Compute the images of all the delta functions in the reduced basis
# We use the rows of LB eigenfunction, which corresponds to the heat
# kernels at every point for an infinitesimal time t. Alternatively, one
# can also use (L1.evecs'*L1.A) and L2.evecs'*L2.A to recover images of
# indicator functions at vertices.
X = np.matmul(C, eVec_1.transpose())
Y = eVec_2.transpose()

# find the nearest point between the mapped delta functions. This gives
# us p2p map
dist, NNIdx = KNearestNeighborsSearch(X.transpose(), Y.transpose(), 1)

# compute p2p map errors
V2_map = V2[NNIdx,:]
error = np.sum(np.power((V2 - V2_map),2),axis=1)
sortError = np.sort(error)

# plot p2p map error
plt.figure()
plt.plot(sortError, np.linspace(0,1,len(error)))
plt.xlabel('Distance error threshold')
plt.ylabel('Fraction of correspondences')
plt.title('Point-to-point map reconstruction error')
plt.show()

