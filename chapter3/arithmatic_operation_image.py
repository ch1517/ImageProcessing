# 강의자료 3-1, 3-2
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

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

im_new3 = np.zeros(shape=(256,256))

for i in range(1,9):
    filename = 'image/noise'+ str(i) +'.bmp'
    im = misc.imread(filename)
    plt.subplot(2,4,i),plt.imshow(im),plt.gray()
    plt.title('Noisy Image: %i'%(i)), plt.axis('off')
    im_new3 = im_new3+np.float32(im)
plt.show()

# 평균값 구하기
im_new3/=8

plt.imshow(im_new3), plt.gray(), plt.title('AVERAGE'), plt.axis('off')
plt.show()