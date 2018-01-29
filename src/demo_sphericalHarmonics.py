import numpy as np
from sph2car import *
from sphericalHarmonics import *
from scatter3 import *

import scipy.special

numAng = 500
m = 0 # degree
l = 0 # level

theta = np.linspace(0, 2*np.pi, num = numAng) # theta
phi = np.linspace(0, np.pi, num = numAng) # phi

thetaGrid, phiGrid = np.meshgrid(theta, phi)
thetaGrid = thetaGrid.flatten()
phiGrid = phiGrid.flatten()
x,y,z = sph2car(thetaGrid, phiGrid)
p = np.concatenate((x[:,None], y[:,None], z[:,None]), axis = 1)

Y = sphericalHarmonics(m,l,thetaGrid,phiGrid)

# check the solution with analytical real SH
# print Y
# print np.sqrt(15/np.pi) / 2 * (p[:,2]*p[:,])

scatter3(p, Y, size = 7, colormap = "default")