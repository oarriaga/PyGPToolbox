from readOBJ import *
from meanCurvature import *
from plotTriMesh import *
from gaussianCurvature import *
from edgeOperator import *

V,F = readOBJ('../meshes/spot.obj')
De, p1234 = edgeOperator(V,F)
print De
print p1234