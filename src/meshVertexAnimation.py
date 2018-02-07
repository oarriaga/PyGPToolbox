import sys
sys.path.append('/usr/local/libigl/python')
import pyigl as igl
from iglhelpers import *

import numpy as np

cIdx = 0
def meshVertexAnimation(V,F,VList,color = np.array([144,210,236]) / 255.0):
	def key_pressed(viewer, key, modifier):
		global cIdx
		if key == ord('r') or key == ord('R'):
			U = VList[:,:,0]
			cIdx = 0
		elif key == ord(' '):
			cIdx += 1
			if cIdx >= VList.shape[2]:
				cIdx = VList.shape[2]-1
			U = VList[:,:,cIdx]
		else:
			return False
		viewer.data.set_mesh(p2e(U.astype(np.float64)), p2e(F.astype(np.int32)))
		return True

	viewer = igl.viewer.Viewer()
	viewer.data.set_mesh(p2e(V.astype(np.float64)), p2e(F.astype(np.int32)))

	c = p2e(np.tile(color[None,:], (V.shape[0], 1)).astype(np.float64))
	viewer.data.set_colors(c)

	backColor = p2e(np.array([1,1,1,1]).astype(np.float64))
	viewer.core.background_color = backColor
	viewer.core.show_lines = False
	viewer.callback_key_pressed = key_pressed

	print("Press [space] to the next mesh.")
	print("Press [r] to reset.")
	print("Press [esc] to close window.")

	viewer.launch()






