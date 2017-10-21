## This code is modified from: https://scipython.com/blog/visualizing-the-bivariate-gaussian-distribution/
## How to use output:
## 	  plt.figure()
## 	  plt.contourf(X, Y, Z)
## 	  plt.show()

# import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def genBivarGaussGrid(mu, cov, numSamples = 60):
	size = np.sqrt(np.amax(cov))
	X = np.linspace(mu[0]-4*size, mu[0]+4*size, numSamples)
	Y = np.linspace(mu[1]-3*size, mu[1]+3*size, numSamples)
	X, Y = np.meshgrid(X, Y)

	pos = np.zeros((X.shape[0], X.shape[1], 2))
	pos[:, :, 0] = X
	pos[:, :, 1] = Y

	def multivariate_gaussian(pos, mu, Sigma):
	    """Return the multivariate Gaussian distribution on array pos.
	    pos is an array constructed by packing the meshed arrays of variables
	    x_1, x_2, x_3, ..., x_k into its _last_ dimension.
	    """
	    n = mu.shape[0]
	    Sigma_det = np.linalg.det(Sigma)
	    Sigma_inv = np.linalg.inv(Sigma)
	    N = np.sqrt((2*np.pi)**n * Sigma_det)
	    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)
	    return np.exp(-fac / 2) / N

	Z = multivariate_gaussian(pos, mu, cov)	
	return X,Y,Z





