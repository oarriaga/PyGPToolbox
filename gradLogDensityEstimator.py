## Reference paper and code: 
## 1. Sasaki et al, "Clustering via Mode Seeking by Direct Estimation of the Gradient of a Log-Density", 2014
## 2. https://sites.google.com/site/hworksites/home/software/lsldg
##
## About how to use the class, please refer to "demo_gradLogDensityEstimation.py"
import numpy as np
import numpy.random
import numpy.linalg

class gradLogDensityEstimator:
	def __init__(self, X, **kwargs):
		## parameter settings
		dim = X.shape[1]
		numSamples = X.shape[0]
		if 'sigmaList' in kwargs: # Gaussian width parameter
			sigmaList = kwargs['sigmaList']
		else:
			sigmaList = np.logspace(-1, 1, num=20)
		if 'lambdaList' in kwargs: # regularization parameter
			lambdaList = kwargs['lambdaList']
		else:
			lambdaList = np.logspace(-2, 1, num=20)
		if 'numCrossValidation' in kwargs: # number of crossvalidation
			numCrossValidation = kwargs['numCrossValidation']
		else:
			numCrossValidation = 5
		if 'gaussCenterIdx' in kwargs:
			C = X[centerIdx, :]
			numBasis = C.shape[0]
		else:
			numBasis = int(numSamples/3)
			centerIdx = numpy.random.randint(numSamples, size=numBasis) # gaussian center indices
			C = X[centerIdx, :]

		## LSLDG (Least-Squares Log-Density Gradient)
		crossValidIdx = numpy.random.randint(numCrossValidation, size=numSamples) # index fro cross validation
		tempC = np.expand_dims(C, axis=1)
		tempX = np.expand_dims(X, axis=0)
		XCDiff = np.tile(tempC, [1,numSamples,1]) - np.tile(tempX, [numBasis,1,1])
		XCDist = np.sum(np.power(XCDiff, 2), axis = 2)

		# compute median of absolute differnce in each dimension
		tempX1 = np.expand_dims(X, axis=1)
		tempX2 = np.expand_dims(X, axis=0)
		XXDiff = np.tile(tempX1, [1,numSamples,1]) - np.tile(tempX2, [numSamples,1,1])
		XXMedian = np.zeros(dim)
		for ii in range(dim):
			XXMedian[ii] = np.median(np.absolute(XXDiff[:,:,ii]).ravel())

		# cross validation
		sigmaOpt = np.zeros(dim)
		lambdaOpt = np.zeros(dim)
		for dd in range(dim):
			crossValidScore = np.zeros((sigmaList.shape[0], lambdaList.shape[0], numCrossValidation))
			for sigmaIdx in range(sigmaList.shape[0]):
				sigmaTemp = XXMedian[dd] * sigmaList[sigmaIdx]
				gaussKernel = np.exp(-XCDist/(2*(sigmaTemp**2)))
				for cvIdx in range(numCrossValidation):
					# cross validation train indices
					idx = np.where(crossValidIdx != cvIdx)[0]
					psiTrain = XCDiff[:,idx,dd] * gaussKernel[:,idx]
					phiTrain = (1 - (XCDiff[:,idx,dd]**2)/(sigmaTemp**2)) * gaussKernel[:,idx]
					kTrain = np.matmul(psiTrain, psiTrain.transpose()) / psiTrain.shape[1]
					hTrain = np.mean(phiTrain, axis=1)

					# cross validation test indices
					idx = np.where(crossValidIdx == cvIdx)[0]
					psiTest = XCDiff[:,idx,dd] * gaussKernel[:,idx]
					phiTest = (1 - (XCDiff[:,idx,dd]**2)/(sigmaTemp**2)) * gaussKernel[:,idx]
					kTest = np.matmul(psiTest, psiTest.transpose()) / psiTest.shape[1]
					hTest = np.mean(phiTest, axis=1)

					for lambdaIdx in range(lambdaList.shape[0]):
						lambdaTemp = lambdaList[lambdaIdx]
						theta_h = numpy.linalg.solve(kTrain + lambdaTemp*np.eye(kTrain.shape[0]), hTrain)
						theta_h = np.expand_dims(theta_h, axis = 1)
						term1 = np.matmul(np.matmul(theta_h.transpose(), kTest),theta_h)[0][0]
						term2 = np.matmul(theta_h.transpose(), np.expand_dims(hTest, axis = 1))[0][0]
						crossValidScore[sigmaIdx, lambdaIdx, cvIdx] = term1 - 2*term2;
			cvScoreMin = np.min(np.mean(crossValidScore,axis=2),axis=1)
			minLambdaIdx = np.argmin(np.mean(crossValidScore,axis=2),axis=1)
			minSigmaIdx = np.argmin(cvScoreMin)
			lambdaOpt[dd] = lambdaList[minLambdaIdx[minSigmaIdx]]
			sigmaOpt[dd] = XXMedian[dd] * sigmaList[minSigmaIdx]
			# print 'dim    =', dd
			# print 'sigma  =', sigmaOpt[dd]
			# print 'lambda =', lambdaOpt[dd]

		# compute theta
		theta = np.zeros((numBasis, dim))
		for dd in range(dim):
		    gaussKernel = np.exp(-XCDist / (2*(sigmaOpt[dd]**2)))
		    psi = XCDiff[:,:,dd] * gaussKernel;
		    phi = (1 - (XCDiff[:,:,dd]**2)/(sigmaOpt[dd]**2)) * gaussKernel
		    k = np.matmul(psi, psi.transpose()) / psi.shape[1]
		    h = np.mean(phi, axis = 1) 
		    theta[:,dd] = numpy.linalg.solve(k + lambdaOpt[dd]*np.eye(k.shape[0]), h)

		## saving estimater parameters
		self.theta = theta
		self.sigma = sigmaOpt
		self.dim = dim
		self.C = C

	def gradEstimate(self, queryPts):
		pts = queryPts
		theta = self.theta
		sigma = self.sigma
		dim = self.dim
		numPts = pts.shape[0]
		numBasis = self.C.shape[0]
		C = self.C

		tempC = np.expand_dims(C, axis=1)
		tempPts = np.expand_dims(pts, axis=0)
		XCDiff = np.tile(tempC, [1,numPts,1]) - np.tile(tempPts, [numBasis,1,1])
		XCDist = np.sum(np.power(XCDiff, 2), axis = 2)
		XCDistTile = np.tile(np.expand_dims(XCDist, axis=2), [1,1,dim])
		twoSigmaSquareTile = np.expand_dims(2*(sigma**2), axis=0)
		twoSigmaSquareTile = np.expand_dims(twoSigmaSquareTile, axis=0)
		twoSigmaSquareTile = np.tile(twoSigmaSquareTile, [XCDist.shape[0],XCDist.shape[1],1])
		gaussKernel3D = np.exp(-XCDistTile / twoSigmaSquareTile)

		psi = XCDiff * gaussKernel3D
		psi = np.swapaxes(psi, 1, 2)
		thetaTile = np.expand_dims(theta, axis = 2)
		thetaTile = np.tile(thetaTile, [1,1,numPts])
		temp = thetaTile * psi
		temp = np.sum(temp, axis = 0)
		gradientPts = temp.transpose()
		return gradientPts



