## Referneces:
## 1. Xu, "Image Smoothing via L0 Gradient Minimization", 2011

import matplotlib.pyplot as plt
import scipy
import scipy.misc
from imageL0Smooth import *

fileName = '../images/lenna.png'
imgSize = 256
lambdaValue = 0.05

I = scipy.misc.imread(fileName) # load image
I = scipy.misc.imresize(I, (imgSize, imgSize)) # resize
I = I / 255.0 # switch [0 255] to [0 1]

S = imageL0Smooth(I, lambdaValue)
plt.subplot(121)
plt.imshow(I)
plt.title('original image')
plt.subplot(122)
plt.imshow(S)
plt.title('l0 minimized image')
plt.show()