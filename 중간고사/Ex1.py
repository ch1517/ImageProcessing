import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
mean=0
#a
for y in range(row):
    for x in range(col):
        mean += im[y,x]
mean=mean/im.size
#b
binary_img=np.where(im>mean,1,0)

#c
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

Num_BitSlice=8
image_BitPlane = np.ndarray(shape=(Num_BitSlice,row,col),dtype=np.uint8)
image_Restore = np.zeros(shape=(row,col),dtype=np.uint8)

#최하위 비트플레인을 레나 이진화 영상으로 대체하기
for y in range(row):
    for x in range(col):
        value=im[y,x]
        c = BitPlane_Slice(value)
        for i in range(Num_BitSlice):
            image_BitPlane[i,y,x]=c[i]
image_BitPlane[Num_BitSlice-1]=binary_img

#이미지 합치기
for i in range(Num_BitSlice):
    image_Restore=image_BitPlane[i]+image_Restore
    
#이미지 저장하기
misc.imsave('lsb_binary_lena.bmp',image_Restore)

#저장된 이미지 불러오기
img = misc.imread('lsb_binary_lena.bmp')
row,col = img.shape
#최하위 비트플레인 출력하기
Num_BitSlice=8
plt.imshow(image_BitPlane[Num_BitSlice-1])
plt.gray()
plt.title('Copyright_Lena')
plt.axis('off')
plt.show()