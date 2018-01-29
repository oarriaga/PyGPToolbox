def rgb2gray(img):
	R = img[:,0]
	G = img[:,1]
	B = img[:,2]
	L = R * 299.0/1000.0 + G * 587.0/1000.0 + B * 114.0/1000.0
	return L