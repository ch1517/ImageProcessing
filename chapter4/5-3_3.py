import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

sigma = 10
g = np.zeros(shape=(9), dtype=np.float)
for x in range(-4,5):
    s=np.sqrt(2*np.pi)*sigma
    v=-pow(x,2)/(2*pow(sigma,2))
    g[x+4]=s*np.exp(v)
plt.plot(g)
plt.show()

sigma = 10
g2 = np.zeros(shape=(9), dtype=np.float)
for x in range(-4,5):
    s=np.sqrt(2*np.pi)*sigma
    v=-pow(x,2)/(2*pow(sigma,2))
    g2[x+4]=s*np.exp(v)
g2 = g2.reshape((9,1))
print((g*g2).shape)

from mpl_toolkits.mplot3d import Axes3D

sigma = 1

x=np.arange(-4,5,0.1)
y=np.arange(-4,5,0.1)
X,Y=np.meshgrid(x,y)

s=1/(2*np.pi*pow(sigma,2))
v=-(pow(X,2)+pow(Y,2))/(2*pow(sigma,2))
g=s*np.exp(v)

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,g)
plt.show()

# 이미지 출력 함수
def image_print(img, title, print_num, current_num):
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')

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

#9*9 가우시안 필터
def Gaussian_FIlter(sigma,Filter_Size):
    g = np.zeros(shape=(Filter_Size,Filter_Size), dtype=np.float)
    for y in range(-4,5):
        for x in range(-4,5):
            s=1/(2*np.pi*pow(sigma,2))
            v=-(pow(x,2)+pow(y,2))/(2*pow(sigma,2))
            g[y+4,x+4]=s*np.exp(v)
    return g

lena = misc.imread('image/lena_256.bmp')
filter_size=9
Image1 = im_filtering(lena, Gaussian_FIlter(1.0,filter_size), filter_size)
Image2 = im_filtering(lena, Gaussian_FIlter(2.0,filter_size), filter_size)
Image3 = im_filtering(lena, Gaussian_FIlter(3.0,filter_size), filter_size)
Image4 = im_filtering(lena, Gaussian_FIlter(4.0,filter_size), filter_size)
Image5 = im_filtering(lena, Gaussian_FIlter(5.0,filter_size), filter_size)

print_num = [2,3]
image_print(lena, "lena",  print_num, 1)
image_print(Image1, "a=1.0",  print_num, 2)
image_print(Image2, "a=2.0",  print_num, 3)
image_print(Image3, "a=3.0",  print_num, 4)
image_print(Image4, "a=4.0",  print_num, 5)
image_print(Image5, "a=5.0",  print_num, 6)

plt.show()