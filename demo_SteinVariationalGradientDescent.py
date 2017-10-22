## Demo of Stein Variational Gradient descent
## Reference: Liu et al, "Stein Variational Gradient Descent (SVGD): A General Purpose Bayesian Inference Algorithm", NIPS 2016

import numpy as np
import numpy.matlib as mat
import numpy.random as random
from numpy.linalg import inv
import matplotlib.pyplot as plt

from steinVGD import *
from genBivarGaussGrid import *
from matplotlib import cm


class multivariateGaussian:
	def __init__(self, mu, cov):
		self.mu = mu
		self.cov = cov
		self.cov_inv = inv(cov)

	def dlogp_dx(self, x):
		# compute derivative of the gaussian log-likelihood (\nabla\log p(x))
		# dlogp_dx = (x-mu) * cov^{-1} 
		dlogp_dx = -np.matmul(x - mat.repmat(self.mu, x.shape[0], 1), self.cov_inv)
		return dlogp_dx

# create a multivariate (2-dim) gaussian distribution as target distribution p(.)
mu = np.array([1.0, 0.5]) # mean
cov = np.array([[0.5, 0.4], [0.3, 0.9]]) # covariance
p = multivariateGaussian(mu, cov)

# create initial particles x
x = np.random.normal(0,0.5, [30, 2]);

# visualize SVGD
gx,gy,gz = genBivarGaussGrid(mu, cov)
plt.figure()
for ii in range(50):
	x = steinVGD(x, p.dlogp_dx, numIter = 50)

	plt.clf()
	plt.contourf(gx, gy, gz, cmap=cm.Blues)
	plt.hold(True)
	plt.scatter(x[:,0], x[:,1], c = 'k')
	plt.pause(0.1)


