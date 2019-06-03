# embedding에서 저장한 lena_w.bmp에 포함된 copyright 이미지 추출하기
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
im = misc.imread('image/lena_w.bmp')
# im = misc.imread('image3/lena_w.jpg')
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

plt.imshow(image_BitPlane[Num_BitSlice-1])
plt.gray()
plt.title('Copyright')
plt.axis('off')
plt.show()
