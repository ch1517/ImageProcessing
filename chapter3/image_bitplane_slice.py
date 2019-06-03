# lena 이미지를 비트별로 나누어 출력하고 다시 하나의 이미지로 합쳐서 출력하여 원본과 비교한다.
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

for i in range(Num_BitSlice):
    plt.subplot(2,4,i+1), plt.imshow(image_BitPlane[i]), plt.gray(), plt.title(i+1), plt.axis('off')
    image_Restore=image_BitPlane[i]+image_Restore
plt.show()

plt.subplot(1,2,1), plt.imshow(im), plt.gray(),plt.title('Original'),plt.axis('off')
plt.subplot(1,2,2), plt.imshow(image_Restore), plt.gray(),plt.title('Restore'),plt.axis('off')
plt.show()