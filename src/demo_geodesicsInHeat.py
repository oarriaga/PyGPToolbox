## Reference:
## Crane et al, "Geodesics in Heat: A New Approach to Computing Distance Based on Heat Flow" 2013

from readOBJ import *
from plotTriMesh import *
from geodesicsInHeat import *

V,F = readOBJ("../meshes/bunny.obj")
centerIdx = 300
D = geodesicsInHeat(V,F,centerIdx)
plotTriMesh(V,F, vertexColor=D, colormap="OrRd")