import numpy as np
from sphericalHarmonics import *
from triMesh import *
from readOBJ import *
from car2sph import *
from vertexAreas import *

m = 1 # degree
l = 2 # level

V,F = readOBJ('../meshes/unitSphere.obj')
phi, theta, r = car2sph(V)
Y = sphericalHarmonics(m,l,phi,theta)

# check the solution with analytical real SH
print "=============="
print "My SH values:"
print Y[10:20]
print "Analytical SH values:"
print (np.sqrt(15/np.pi) / 2 * (V[:,2]*V[:,0]))[10:20]

# check orthogonality
print "=============="
print "dot product between different SH (should be 0)"
print np.sum(Y * sphericalHarmonics(2,3,phi,theta))

# check orthonormal
print "=============="
print "dot product between the same SH (should be 1)"
VA = vertexAreas(V,F)
print np.sum(Y * VA * Y)
# above computation is equavalent to below
# M = np.diag(VA)
# print Y[None,:].dot(M).dot(Y[:,None])[0,0]

triMesh(V,F,Y, colormap = "default")

# =======
#   RIP
# =======
# import numpy as np
# from sph2car import *
# from sphericalHarmonics import *
# from scatter3 import *
# 
# theta = np.linspace(0, 2*np.pi, num = numAng) # theta
# phi = np.linspace(0, np.pi, num = numAng) # phi
# thetaGrid, phiGrid = np.meshgrid(theta, phi)
# thetaGrid = thetaGrid.flatten()
# phiGrid = phiGrid.flatten()
# x,y,z = sph2car(thetaGrid, phiGrid)
# p = np.concatenate((x[:,None], y[:,None], z[:,None]), axis = 1)