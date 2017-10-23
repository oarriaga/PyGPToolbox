## Reference: Sasaki et al, "Clustering via Mode Seeking by Direct Estimation of the Gradient of a Log-Density", 2014

import numpy as np
import numpy.random
import matplotlib.pyplot as plt
from gradLogDensityEstimator import *

## generate data
mean = np.array([4,2])
cov = np.array([[2, 0],[0, 0.5]])
X1 = np.random.multivariate_normal(mean, cov, 100)
mean = np.array([4,-2])
cov = np.array([[2, 0],[0, 0.5]])
X2 = np.random.multivariate_normal(mean, cov, 100);
mean = np.array([-4,0])
cov = np.array([[0.5, 0],[0, 2]])
X3 = np.random.multivariate_normal(mean, cov, 300);
trainData = np.concatenate((X1, X2, X3), axis=0)

## plot generated data
# plt.scatter(X[:,0], X[:,1])
# plt.axis('equal')
# plt.show()

## create query points
numX = 30
numY = 24
X = np.linspace(-6, 8, numX)
Y = np.linspace(-6, 6, numY)
X, Y = np.meshgrid(X, Y)
pts = np.concatenate((X.reshape([numX*numY,1]), Y.reshape([numX*numY,1])), axis=1)

## create gradient estimator
model = gradLogDensityEstimator(trainData)
grad = model.gradEstimate(pts)

## plot estimation results
grad = grad * 0.2 # shrink the gradient for visualization purpose
gradX = np.concatenate((pts[:,0:1], pts[:,0:1] + grad[:,0:1]), axis=1).transpose()
gradY = np.concatenate((pts[:,1:2], pts[:,1:2] + grad[:,1:2]), axis=1).transpose()

plt.figure()
plt.title('gradient of the log-PDF (probability density function)')
plt.hold(True)
plt.scatter(trainData[:,0], trainData[:,1], color='k', s = 4)
plt.plot(gradX, gradY, color = 'r', linewidth=0.7)
plt.show()





