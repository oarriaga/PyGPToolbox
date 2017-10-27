## A demo of conformal MCF
## Reference: 
## Kazhdan et al, "Can Mean-Curvature Flow be Modified to be Non-singular?", 2012

import numpy as np
from mayavi import mlab
from readOBJ import *
from conformalMeanCurvatureFlow import *

V,F = readOBJ('../meshes/fandisk.obj')
numMCFIter = 100
stepSize = 0.0005 # step size needs to be sufficiently small
V_MCF = conformalMeanCurvatureFlow(V,F,stepSize,numMCFIter)

# make animation
@mlab.show
@mlab.animate(delay=50, ui=True)
def anim():
	mlab.figure(bgcolor = (1,1,1))
	color = (6.0/ 155.0, 41.0/ 155.0, 88.0/ 155.0) 
	fig = mlab.triangular_mesh(V_MCF[:,0,1], V_MCF[:,1,1], V_MCF[:,2,1], F, color=color)
	ii = 1
	while True:
	    fig.mlab_source.set(x=V_MCF[:,0,ii], y=V_MCF[:,1,ii], z=V_MCF[:,2,ii])
	    ii += 1
	    if ii == numMCFIter:
	    	ii = 1
	    yield
anim()
