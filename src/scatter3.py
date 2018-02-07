import sys
sys.path.append('/usr/local/libigl/python') # "path/to/libigl/python"
import pyigl as igl
from iglhelpers import *

from colorMap import *

def scatter3(p, c = np.array([0]), size = 3, colormap = "default"):
	if (c.shape[0] != p.shape[0]):
		c = np.zeros((p.shape[0],3)) + 0.7
		color = p2e(c.astype(np.float64))
	elif ((c.shape[0] == p.shape[0]) and colormap == "jet"):
		color = igl.eigen.MatrixXd()
		igl.jet(p2e(c.astype(np.float64)), True, color)
	elif c.shape == p.shape:
		color = p2e(c.astype(np.float64))
	else:
		from colorMap import *
		# colormap: "blue", "red", "green", "default"
		color = colorMap(c, colormap = colormap)
		color = p2e(color.astype(np.float64))

	backColor = p2e(np.array([1,1,1,1]).astype(np.float64))
	viewer = igl.viewer.Viewer()
	viewer.data.set_points(p2e(p.astype(np.float64)), color)
	viewer.core.point_size = size
	viewer.core.background_color = backColor
	viewer.launch()