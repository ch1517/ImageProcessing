# 3-3 영상의 뺄셈
# h(x,y)=f(x,y)-g(x,y)
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

#Image Read
hole=misc.imread('image/hole2.bmp')
lena=misc.imread('image/lena_256.bmp')

hole2 = np.float32(hole)
lena2 = np.float32(lena)

im_new1 = np.uint8(np.where(lena2-hole2<0,0,lena2-hole2))
im_new2 = np.uint8(np.where(hole2-lena2<0,0,hole2-lena2))

plt.subplot(2,3,1), plt.imshow(lena), plt.gray(), plt.title('Lena Image'), plt.axis('off')
plt.subplot(2,3,2), plt.imshow(hole), plt.gray(), plt.title('Hole Image'), plt.axis('off')
plt.subplot(2,3,3), plt.imshow(im_new1), plt.gray(), plt.title('Sub Image'), plt.axis('off')
plt.subplot(2,3,4), plt.imshow(hole), plt.gray(), plt.title('Hole Image'), plt.axis('off')
plt.subplot(2,3,5), plt.imshow(lena), plt.gray(), plt.title('Lena Image'), plt.axis('off')
plt.subplot(2,3,6), plt.imshow(im_new2), plt.gray(), plt.title('Sub Image'), plt.axis('off')

plt.show()