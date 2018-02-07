import sys
sys.path.append('/usr/local/libigl/python')
import pyigl as igl
from iglhelpers import *

import numpy as np

from colorMap import *

# my code
cIdx = 0
def meshColorAnimation(V,F,colorList,colormap = 'default'):
	colorList = np.ascontiguousarray(colorList, dtype=np.float64)
	def transformColors(c, colormap):
		if colormap == "jet":
			color = igl.eigen.MatrixXd()
			igl.jet(p2e(c.astype(np.float64)), True, color)
		else:
			# colormap: "blue", "red", "green", "default"
			color = colorMap(c, colormap = colormap)
			color = p2e(color.astype(np.float64))
		return color
	
	def key_pressed(viewer, key, modifier):
		global cIdx
		if key == ord('r') or key == ord('R'):
			c = colorList[:,0]
			cIdx = 0
			color = transformColors(c, colormap)
		elif key == ord(' '):
			cIdx += 1
			if cIdx >= colorList.shape[1]:
				cIdx = colorList.shape[1]-1
			c = colorList[:,cIdx]
			color = transformColors(c, colormap)
		else:
			return False
		viewer.data.set_colors(color)
		return True

	viewer = igl.viewer.Viewer()
	viewer.data.set_mesh(p2e(V.astype(np.float64)), p2e(F.astype(np.int32)))
	
	c = colorList[:,0]
	color = transformColors(c, colormap)
	viewer.data.set_colors(color)
	backColor = p2e(np.array([1,1,1,1]).astype(np.float64))
	viewer.core.background_color = backColor
	viewer.core.show_lines = False
	viewer.callback_key_pressed = key_pressed

	print("Press [space] to the next color.")
	print("Press [r] to reset.")
	print("Press [esc] to close window.")

	viewer.launch()




