import numpy as np
import scipy.special

# phi: angle between positive z-axis
# theta: angle from positive x-axis

def sphericalHarmonics(m,l,phi,theta):
	P = scipy.special.lpmv(abs(m),l,np.cos(theta))
	K = -1**m * np.sqrt( (2*l+1)*scipy.special.factorial(l-abs(m)) / (4*np.pi*scipy.special.factorial(l+abs(m))) )
	if m > 0:
		Y = K * np.sqrt(2) * P * np.cos(abs(m) * phi)
	elif m < 0:
		Y = K * np.sqrt(2) * P * np.sin(abs(m) * phi)
	else: # m == 0
		Y = np.sqrt((2*l+1) / (4*np.pi))* P
	return Y
