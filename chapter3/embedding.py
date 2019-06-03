# copyright가 포함된 레나 이미지 만들기

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)] ) )
def BitPlane_Slice(value):
    c = np.zeros(8)
    n = 7
    bits = bin8(value)
    for i in range(8):
        p = pow(2, n)
        c[i] = p * int(bits[i])
        n = n - 1
    return c
im = misc.imread('image/lena_256.bmp')
copyright = misc.imread('image/copyright.bmp')
row,col = im.shape
Num_BitSlice=8
image_BitPlane = np.ndarray(shape=(Num_BitSlice,row,col),dtype=np.uint8)
image_Restore = np.zeros(shape=(row,col),dtype=np.uint8)

for y in range(row):
    for x in range(col):
        value=im[y,x]
        c = BitPlane_Slice(value)
        for i in range(Num_BitSlice):
            image_BitPlane[i,y,x]=c[i]
image_BitPlane[Num_BitSlice-1]=copyright

for i in range(Num_BitSlice):
    plt.subplot(2,4,i+1), plt.imshow(image_BitPlane[i]), plt.gray(), plt.title(i+1), plt.axis('off')
    image_Restore=image_BitPlane[i]+image_Restore
plt.show()

plt.subplot(1,3,1), plt.imshow(im), plt.gray(),plt.title('Original'),plt.axis('off')
plt.subplot(1,3,2), plt.imshow(copyright), plt.gray(),plt.title('copyright'),plt.axis('off')
plt.subplot(1,3,3), plt.imshow(image_Restore), plt.gray(),plt.title('Restore'),plt.axis('off')
plt.show()

misc.imsave('image/lena_w.bmp',image_Restore)
misc.imsave('image/lena_w.jpg',image_Restore)