from readOBJ import *
from vertArea import *
from cotanLaplace import *
from adjacencyMat import *
from plotTriMesh import *

V,F = readOBJ('./meshes/fandisk.obj')
VA = vertArea(V, F)
L = cotanLaplace(V,F)
A = adjacencyMat(F)

##from mpl_toolkits.mplot3d import Axes3D
##from mpl_toolkits.mplot3d.art3d import Poly3DCollection
##
##
##import matplotlib.pyplot as plt
##fig = plt.figure(figsize=plt.figaspect(0.5))
##ax = fig.add_subplot(1, 2, 1, projection='3d')
##ax.plot_trisurf(V[:,0], V[:,1], V[:,2], triangles=F)
##plt.show()

# from mayavi import mlab
# mlab.clf()
# mlab.triangular_mesh(V[:,0], V[:,1], V[:,2], F)
# mlab.show()

plotTriMesh(V,F, faceColor = VA, opacity=0.7)
