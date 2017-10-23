## A demo of implicit MCF
## Reference: Desbrun et al, "Implicit fairing of irregular meshes using diffusion and curvature flow", 1999

import numpy as np
from mayavi import mlab
from readOBJ import *
from implicitMeanCurvatureFlow import *

V,F = readOBJ('./meshes/fandisk.obj')
numMCFIter = 60
stepSize = 0.0005 # step size needs to be sufficiently small
V_MCF = implicitMeanCurvatureFlow(V,F,stepSize,numMCFIter)

# make animation
@mlab.show
@mlab.animate(delay=30, ui=True)
def anim():
	mlab.figure(bgcolor = (1,1,1))
	color = (6.0/ 155.0, 41.0/ 155.0, 88.0/ 155.0) 
	fig = mlab.triangular_mesh(V[:,0], V[:,1], V[:,2], F, color=color)
	ii = 1
	while True:
	    fig.mlab_source.set(x=V_MCF[:,0,ii], y=V_MCF[:,1,ii], z=V_MCF[:,2,ii])
	    ii += 1
	    if ii == numMCFIter:
	    	ii = 1
	    yield
anim()
