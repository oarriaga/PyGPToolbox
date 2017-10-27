## Inputs:
## array1: N-by-D numpy array contains N data points in D dimensions
## array2: M-by-D numpy array contains M data points in D dimensions
## k: number of neighbors to return
##
## Output:
## dist: distance between the point in array1 with kNN
## NNIdx: nearest neighbor indices of array1

import scipy
import scipy.spatial

def KNearestNeighborsSearch(array1, array2, k):
	kdtree = scipy.spatial.cKDTree(array2)
	dist, NNIdx = kdtree.query(array1, k)
	return dist, NNIdx