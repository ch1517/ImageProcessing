# 라플라시안 필터링 프로그램
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

# Embossing_Filter1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
# Embossing_Filter2=np.array([[1,1,1],[1,-8,1],[1,1,1]])

Embossing_Filter1=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
Embossing_Filter2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
lena = misc.imread('image/medical.bmp')
Filter_Size = 3
Image_New1 = im_filtering(lena, Embossing_Filter1, Filter_Size)
Image_New2 = im_filtering(lena, Embossing_Filter2, Filter_Size)

plt.subplot(1,3,1);
plt.title("original")
plt.gray()
plt.axis('off')
plt.imshow(lena)

plt.subplot(1,3,2);
plt.title("camera 4")
plt.gray()
plt.imshow(Image_New1)
plt.axis('off')

plt.subplot(1,3,3);
plt.title("camera 8")
plt.gray()
plt.imshow(Image_New2)
plt.axis('off')
plt.show()