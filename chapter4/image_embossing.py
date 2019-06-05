# 레나 이미지 엠보싱
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

def im_filtering(im, Filter, FilterSize):
    row, col = im.shape
    padding=int(FilterSize/2)

    Image_Buffer = np.zeros(shape=(row,col), dtype=np.uint8)

    Image_Buffer2 = np.zeros(shape=(row+2*padding,col+2*padding), dtype=np.uint8)
    Image_Buffer2[padding:row+padding, padding:col+padding] = im[:,:]
    Image_New = np.zeros(shape=(row,col), dtype=np.uint8)
    for y in range(padding,row+padding):
        for x in range(padding,col+padding):
            buff = Image_Buffer2[y-padding:y+padding+1,x-padding:x+padding+1]
            pixel = np.sum(buff * Filter)
            pixel = np.uint8(np.where(pixel>255,255,np.where(pixel<0,0,pixel)))
            Image_New[y-padding,x-padding] = pixel
    return Image_New

Embossing_Filter=np.array([[-1,0,0],[0,0,0],[0,0,1]])
lena = misc.imread('image/lena_256.bmp')
Filter_Size = 3
Image_New = im_filtering(lena, Embossing_Filter, Filter_Size)
Image_New = Image_New+128

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.axis('off')
plt.imshow(lena)

plt.subplot(1,2,2);
plt.title("embossing")
plt.gray()
plt.imshow(Image_New)
plt.axis('off')
plt.show()