from mayavi import mlab

def plotTriMesh(V,F,**kwargs):
	if 'color' in kwargs:
		# color must be a single triple between [0.0,1.0], for example, (0.5,0.5,0.5) 
		color = kwargs['color']
		mlab.triangular_mesh(V[:,0], V[:,1], V[:,2], F, color=color)
		mlab.show()
	else:
		mlab.triangular_mesh(V[:,0], V[:,1], V[:,2], F)
		mlab.show()