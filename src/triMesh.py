import sys
sys.path.append('/usr/local/libigl/python') # "path/to/libigl/python"
import pyigl as igl
from iglhelpers import *

from colorMap import *

def triMesh(V,F,c = np.array([0]), colormap = "default"):
	if (c.shape[0] != V.shape[0]):
		c = np.zeros((V.shape[0],3)) + 0.7
		color = p2e(c.astype(np.float64))
	elif ((c.shape[0] == V.shape[0]) and colormap == "jet"):
		color = igl.eigen.MatrixXd()
		igl.jet(p2e(c.astype(np.float64)), True, color)
	else:
		# colormap: "blue", "red", "green", "default"
		color = colorMap(c, colormap = colormap)
		color = p2e(color.astype(np.float64))

	viewer = igl.viewer.Viewer()
	viewer.data.set_mesh(p2e(V.astype(np.float64)), p2e(F.astype(np.int32)))
	viewer.core.show_lines = False
	viewer.data.set_colors(color)
	viewer.launch()
