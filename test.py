from readOBJ import *
from vertexAreas import *
from vertexNormals import *
from faceAreas import *
from faceNormals import *

V,F = readOBJ('./meshes/fandisk.obj')
VA = vertexAreas(V, F)
VN = vertexNormals(V,F)
FA = faceAreas(V,F)
FN = faceNormals(V,F)

from cotanLaplace import *
from adjacencyMat import *

L = cotanLaplace(V,F)
A = adjacencyMat(F)



