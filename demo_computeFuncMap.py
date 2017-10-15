from readOBJ import *
from cotanLaplace import *
from vertArea import *
import scipy
import scipy.sparse
import scipy.sparse.linalg
import matplotlib.pyplot as plt 


V1,F1 = readOBJ('./meshes/tr_reg_089.obj')
V2,F2 = readOBJ('./meshes/tr_reg_090.obj')

# compute laplace eigenbases
numEigs = 30

VA = vertArea(V1, F1)
L = cotanLaplace(V1,F1)
massMat_1 = scipy.sparse.csr_matrix(np.diag(VA))
eVal_1, eVec_1 = scipy.sparse.linalg.eigsh(L, M=massMat_1, k=numEigs, which='LM',sigma = 0)

VA = vertArea(V2, F2)
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

plt.imshow(C)
plt.show()
