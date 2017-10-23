## demo of heat kernel signature
##
## Reference:
## 1. Sun et al, "A Concise and Provably Informative Multi-Scale Signature Based on Heat Diffusion" 2009
## 2. Bronstein et al, "Scale-invariant heat kernel signatures for non-rigid shape recognition", 2010

from readOBJ import *
from heatKernelSignature import *
from animateVertexColor import *

# load data
V,F = readOBJ('./meshes/spot.obj')

# heatKernelSignature(V,F,numEigs,logtmax,logtmin,numTimeSteps)
HKS = heatKernelSignature(V,F, 300, 4, -2, 100)

# plot HKS
delayTime = 70
animateVertexColor(V,F,HKS[:,:60], delayTime)