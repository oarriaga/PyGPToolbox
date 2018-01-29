from sqrt3Subdivision import *
from readOBJ import *

from triMesh import *

V,F = readOBJ('../meshes/fandisk.obj')
V,F = sqrt3Subdivision(V,F)
triMesh(V,F)
