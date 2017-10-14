## Inputs:
## V: n-by-3 numpy ndarray of vertex positions
## F: n-by-3 numpy ndarray of face indices
## opacity: [0.0~1.0] representing opacity
## vertexColor: |V|-by-1 numpy array between [0,1]
## faceColor: |F|-by-1 numpy array between [0,1]
##
## Example:
## plotTriMesh(V,F, vertexColor = CData, opacity = 0.7)

from mayavi import mlab

def plotTriMesh(V,F,**kwargs):
	# opacity 
	if 'opacity' in kwargs:
		opacity = kwargs['opacity']
	else:
		opacity = 1.0

	# color 
	if 'vertexColor' in kwargs:
		color = kwargs['vertexColor']
		mesh = mlab.pipeline.triangular_mesh_source(V[:,0],V[:,1],V[:,2],F)
		point_data = mesh.mlab_source.dataset.point_data
		point_data.scalars = color
		point_data.scalars.name = 'Point data'
		mesh.mlab_source.update()
		mesh2 = mlab.pipeline.set_active_attribute(mesh, point_scalars='Point data')
		mlab.pipeline.surface(mesh2,opacity = opacity)
	elif 'faceColor' in kwargs:
		color = kwargs['faceColor']
		mesh = mlab.pipeline.triangular_mesh_source(V[:,0],V[:,1],V[:,2],F)
		cell_data = mesh.mlab_source.dataset.cell_data
		cell_data.scalars = color
		cell_data.scalars.name = 'Cell data'
		mesh.mlab_source.update()
		mesh2 = mlab.pipeline.set_active_attribute(mesh, cell_scalars='Cell data')
		mlab.pipeline.surface(mesh2, opacity = opacity)
	else:
		color = (6.0/ 155.0, 41.0/ 155.0, 88.0/ 155.0) 
		mlab.triangular_mesh(V[:,0], V[:,1], V[:,2], F, color=color, opacity = opacity)
	mlab.show()