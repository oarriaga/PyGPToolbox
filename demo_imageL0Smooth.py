## Referneces:
## 1. Xu, "Image Smoothing via L0 Gradient Minimization", 2011

import matplotlib.pyplot as plt
from imageL0Smooth import *

fileName = './images/lenna.png'
imgSize = 256
lambdaValue = 0.05

img = imageL0Smooth(fileName, imgSize, lambdaValue)
plt.imshow(img)
plt.show()