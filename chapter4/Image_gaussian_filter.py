# sigma 1~5까지의 가우시안필터 적용 이미지를 원본 이미지와 비교한다.
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

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
Filter_Size = 9

plt.subplot(2,3,1),plt.title("original"),plt.gray(),plt.axis('off'),plt.imshow(lena)
for i in range(1,6):
    Image_New = im_filtering(lena, Gaussian_FIlter(i,Filter_Size), Filter_Size)
    plt.subplot(2,3,i+1),plt.title("sigma=%d" %i),plt.gray(),plt.axis('off'),plt.imshow(Image_New)

plt.show()