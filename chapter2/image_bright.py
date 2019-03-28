# 나. 영상의 밝기조절
# g(x,y)=f(x,y)+n
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape

num = 50
im_bright = im + num
im_dark = im - num
im_bright2=np.where((im+num)>255,255,im+num)
im_dark2=np.where((im-num)<0,0,im-num)
plt.subplot(1,3,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,3,2);
plt.title("bright")
plt.gray()
plt.imshow(im_bright2)
plt.axis('off')

plt.subplot(1,3,3);
plt.title("dark")
plt.gray()
plt.imshow(im_dark2)
plt.axis('off')
plt.show()