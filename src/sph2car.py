# convert spherical coordinate to cartesian coordinate
# phi: angle between positive z-axis
# theta: angle from positive x-axis

import numpy as np

def sph2car(theta, phi, r = 1):
	r_xy = r * np.sin(phi)
	x = r_xy * np.cos(theta)
	y = r_xy * np.sin(theta)
	z = r * np.cos(phi)
	return x, y, z