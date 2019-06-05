# 이미지에 필터를 적용하는 프로그램
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

lena = misc.imread('image/lena_256.bmp')
row, col = lena.shape

# Identity_Filter=np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])

Filter_Size = 5
padding=int(Filter_Size/2)
Identity_Filter=np.zeros(shape=(Filter_Size,Filter_Size))
Identity_Filter[padding,padding]=1

Image_Buffer = np.zeros(shape=(row,col), dtype=np.uint8)

padding= int(len(Identity_Filter[0])/2) # 제외 범위
ft_size= int(len(Identity_Filter[0])/2) # 필터 사이즈/2

Image_Buffer2 = np.zeros(shape=(row+2*padding,col+2*padding), dtype=np.uint8)
Image_Buffer2[padding:row+padding, padding:col+padding] = lena[:,:]
Image_New = np.zeros(shape=(row,col), dtype=np.uint8)
for y in range(padding,row+padding):
    for x in range(padding,col+padding):
        # sum=0
        # for i in range(-ft_size,ft_size+1):
        #     for j in range(-ft_size,ft_size+1):
        #         sum=sum+Identity_Filter[j][i]*lena[x-j][y-i]
        # Image_Buffer[x][y]=sum
        buff = Image_Buffer2[x-padding:x+padding+1,y-padding:y+padding+1]
        pixel = np.sum(buff * Identity_Filter)
        pixel = np.uint8(np.where(pixel>255,255,np.where(pixel<0,0,pixel)))
        Image_New[x-padding,y-padding] = pixel
plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.axis('off')
plt.imshow(lena)

plt.subplot(1,2,2);
plt.title("lena2")
plt.gray()
plt.imshow(Image_New)
plt.axis('off')
plt.show()