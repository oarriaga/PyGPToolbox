import numpy as np
from scatter3 import *

def colorMap(x, colormap = "default"):
	if colormap == "blue":
		baseColor = np.array([[247,251,255],
			[222,235,247],[198,219,239],
			[158,202,225],[107,174,214],
			[ 66,146,198],[ 33,113,181],
			[  8, 81,156],[  8, 48,107]])
	elif colormap == "red":
		baseColor = np.array([[255,255,204],
			[255,237,160],[254,217,118],
			[254,178,76],[253,141,60],
			[ 252,78,43],[ 227,26,28],
			[  189, 0,38],[  128, 0,38]])
	elif colormap == "green":
		baseColor = np.array([[247,252,245],
			[229,245,224],[199,233,192],
			[161,217,155],[116,196,118],
			[ 65,171, 93],[35,139, 69],
			[  0,109, 44],[ 0, 68,27]])
	else: # default
		baseColor = np.array([[215,48,39],
			[244,109,67],[253,174,97],
			[254,224,144],[255,255,191],
			[224,243,248],[171,217,233],
			[116,173,209],[69,117,180]])

	x -= x.min()
	x /= (x.max()+1e-16)

	xp = np.linspace(0,1,num = 9)

	r_fp = baseColor[:,0]
	g_fp = baseColor[:,1]
	b_fp = baseColor[:,2]

	r = np.interp(x, xp, r_fp)
	g = np.interp(x, xp, g_fp)
	b = np.interp(x, xp, b_fp)
	color = np.concatenate((r[:,None],g[:,None],b[:,None]), 1) / 256.0
	return color