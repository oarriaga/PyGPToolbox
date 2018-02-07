## demo of kernel signatures (HKS or WKS)
## please comment/uncomment the section you want
##
## Reference:
## 1. Sun et al, "A Concise and Provably Informative Multi-Scale Signature Based on Heat Diffusion" 2009
## 2. Bronstein et al, "Scale-invariant heat kernel signatures for non-rigid shape recognition", 2010

from readOBJ import *
from heatKernelSignature import *
from waveKernelSignature import *
# from animateVertexColor import *
from waveKernelMap import *
from meshColorAnimation import *

# load data
V,F = readOBJ('../meshes/spot.obj')

## 1. heatKernelSignature(V,F,numEigs,logtmax,logtmin,numTimeSteps)
# HKS = heatKernelSignature(V,F, 300, 4, -2, 100)
# meshColorAnimation(V,F,HKS[:,:60],colormap = 'red')

# delayTime = 70
# animateVertexColor(V,F,HKS[:,:60], delayTime, colormap = "OrRd")

## 2. waveKernelSignature(V,F,numEigs, numTimeSteps)
WKS = waveKernelSignature(V,F, 300, 200)
meshColorAnimation(V,F,WKS,colormap = 'blue')

# delayTime = 35
# animateVertexColor(V,F,WKS, delayTime)

## 3. waveKernelMap(V,F,numEigs, numTimeSteps)
# landmarks = np.random.randint(V.shape[0], size=10)
# WKS = waveKernelMap(V,F, landmarks, 300, 200)
# meshColorAnimation(V,F,WKS,colormap = 'blue')

# delayTime = 35
# animateVertexColor(V,F,WKS, delayTime)
