import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
from mpl_toolkits.mplot3d import Axes3D

sigma = 30

x=np.arange(-128,127,1.0)
y=np.arange(-128,127,1.0)
X,Y=np.meshgrid(x,y)

s=1/(np.pi*pow(sigma,4))
a=-(pow(X,2)+pow(Y,2))/(2*pow(sigma,2))
g=-s*(1+a)*np.exp(a)

#a
plt.imshow(g)
plt.gray()
plt.title('LoG(x,y)')
plt.axis('off')
plt.show()

#b
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,g)
plt.show()

#c
#9*9 LoG 필터
def LoG_FIlter(sigma,Filter_Size):
    g = np.zeros(shape=(Filter_Size,Filter_Size), dtype=np.float)
    for y in range(-4,5):
        for x in range(-4,5):
            s=1/(np.pi*pow(sigma,4))
            a=-(pow(x,2)+pow(y,2))/(2*pow(sigma,2))
            p=-s*(1+a)*np.exp(a)
            g[y+4,x+4]=p
    return g
Filter_Size = 9
print(LoG_FIlter(0.8,Filter_Size))

#d

def im_filtering(im, Filter, FilterSize):
    row, col = im.shape
    padding=int(FilterSize/2)

    Image_Buffer = np.zeros(shape=(row+2*padding,col+2*padding), dtype=np.uint8)
    Image_Buffer[padding:row+padding, padding:col+padding] = im[:,:]
    Image_New = np.zeros(shape=(row,col), dtype=np.uint8)
    for y in range(padding,row+padding):
        for x in range(padding,col+padding):
            buff = Image_Buffer[y-padding:y+padding+1,x-padding:x+padding+1]
            pixel = np.sum(buff * Filter)
            pixel = np.uint8(np.where(pixel>255,255,np.where(pixel<0,0,pixel)))
            Image_New[y-padding,x-padding] = pixel
    return Image_New

lena = misc.imread('image/lena_256.bmp')
filtering_img = im_filtering(lena, LoG_FIlter(0.8,Filter_Size), Filter_Size)

# 이미지 출력 함수
def image_print(img, title, print_num, current_num):
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')

print_num = [1,2]
image_print(lena, "InputImage",  print_num, 1)
image_print(filtering_img, "Log Filtering Image",  print_num, 2)
plt.show()