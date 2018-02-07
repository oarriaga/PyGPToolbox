# convert spherical coordinate to cartesian coordinate
# theta: angle between positive z-axis
# phi: angle from positive x-axis

import numpy as np

def sph2car(phi, theta, r = 1):
	r_xy = r * np.sin(theta)
	x = r_xy * np.cos(phi)
	y = r_xy * np.sin(phi)
	z = r * np.cos(theta)
	return x, y, z