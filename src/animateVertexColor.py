from mayavi import mlab

def animateVertexColor(V,F,VColor, delay = 50, **kwargs):
	# opacity 
	if 'opacity' in kwargs:
		opacity = kwargs['opacity']
	else:
		opacity = 1.0
	# colormap
	if 'colormap' in kwargs:
		colormap = kwargs['colormap']
	else:
		colormap = "Blues"

	numSteps = VColor.shape[1]
	
	@mlab.show
	@mlab.animate(delay=delay, ui=True)
	def anim():
		mlab.figure(bgcolor = (1,1,1))
		mesh = mlab.pipeline.triangular_mesh_source(V[:,0],V[:,1],V[:,2],F)
		point_data = mesh.mlab_source.dataset.point_data
		point_data.scalars = VColor[:,0]
		point_data.scalars.name = 'Point data'
		mesh.mlab_source.update()
		mesh = mlab.pipeline.set_active_attribute(mesh, point_scalars='Point data')
		mlab.pipeline.surface(mesh, opacity = opacity, colormap = colormap)
		# for ii in range(numSteps):
		# 	point_data = mesh.mlab_source.dataset.point_data
		# 	point_data.scalars = VColor[:,ii]
		# 	point_data.scalars.name = 'Point data'
		# 	mesh.mlab_source.update()
		# 	yield
		ii = 0
		while True:
			point_data = mesh.mlab_source.dataset.point_data
			point_data.scalars = VColor[:,ii]
			point_data.scalars.name = 'Point data'
			mesh.mlab_source.update()
			ii += 1
			if ii == VColor.shape[1]:
				ii = 0
			yield

	anim()
	