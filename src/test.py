from readOBJ import *
from meanCurvature import *
# from plotTriMesh import *
from gaussianCurvature import *
from dihedralAngleMat import *

V,F = readOBJ('../meshes/fandisk.obj')
A = dihedralAngleMat(V,F)
print A