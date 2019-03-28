# 다. 영상의 명암비 조절
# g(x,y)=(f(x,y)-128)*a
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
a=0.1
m = np.mean(im)
im_contrast = im+(im-m)*a

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("contrast")
plt.gray()
plt.imshow(im_contrast)
plt.axis('off')

plt.show()