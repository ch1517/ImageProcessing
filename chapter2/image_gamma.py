# 라. 감마 보정(gamma correction)
# g(x,y) = M(f(x,y)/M)^(1/r)
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
r=0.6
m=255
im_gammaCorrection = m*np.power((im/m),1/r)

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("Gamma Correction")
plt.gray()
plt.imshow(im_gammaCorrection)
plt.axis('off')

plt.show()