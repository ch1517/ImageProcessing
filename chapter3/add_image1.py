# 3-1 영상의 덧셈
# h(x,y) = f(x,y)+g(x,y)
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

#Image Read
aero=misc.imread('image/aero2.bmp')
hole=misc.imread('image/hole.bmp')
lena=misc.imread('image/lena_256.bmp')

#Overflow 방지
aero2 = np.float32(aero)
hole2 = np.float32(hole)
lena2 = np.float32(lena)

im_new1 = np.uint8(np.where(lena2+aero2>255,255,lena2+aero2))
im_new2 = np.uint8(np.where(lena2+hole2>255,255,lena2+hole2))

plt.subplot(2,3,1), plt.imshow(aero), plt.gray(), plt.title('AERO Image'), plt.axis('off')
plt.subplot(2,3,2), plt.imshow(lena), plt.gray(), plt.title('ADD Result'), plt.axis('off')
plt.subplot(2,3,3), plt.imshow(im_new1), plt.gray(), plt.title('AERO Image'), plt.axis('off')
plt.subplot(2,3,4), plt.imshow(lena), plt.gray(), plt.title('LENA Image'), plt.axis('off')
plt.subplot(2,3,5), plt.imshow(hole), plt.gray(), plt.title('HOLE Image'), plt.axis('off')
plt.subplot(2,3,6), plt.imshow(im_new2), plt.gray(), plt.title('ADD Result'), plt.axis('off')
plt.show()