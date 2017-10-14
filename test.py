from readOBJ import *
from vertArea import *
from cotanLaplace import *
from adjacencyMat import *

V,F = readOBJ('./meshes/fandisk.obj')
VA = vertArea(V, F)
L = cotanLaplace(V,F)
A = adjacencyMat(F)
