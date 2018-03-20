import sys
sys.path.append('/usr/local/libigl/python') # "path/to/libigl/python"
import pyigl as igl
from iglhelpers import *

def triMeshTextured(V,F,TV,TF,PNGFileName):
	R = igl.eigen.MatrixXuc()
	G = igl.eigen.MatrixXuc()
	B = igl.eigen.MatrixXuc()
	A = igl.eigen.MatrixXuc()
	igl.png.readPNG(PNGFileName, R, G, B, A)

	V = np.ascontiguousarray(V, dtype=np.float64)
	TV = np.ascontiguousarray(TV, dtype=np.float64)
	
	viewer = igl.viewer.Viewer()
	viewer.data.set_mesh(p2e(V), p2e(F.astype(np.int32)))
	viewer.core.show_lines = False
	viewer.data.set_uv(p2e(TV),p2e(TF.astype(np.int32)))
	viewer.core.show_texture = True
	viewer.data.set_texture(R,G,B)
	viewer.data.set_colors(p2e(np.ones((V.shape[0],4), dtype = np.float64)))
	backColor = p2e(np.array([1,1,1,1]).astype(np.float64))
	viewer.core.background_color = backColor
	viewer.launch()