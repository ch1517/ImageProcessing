# 2. lena 영상을 이용하여 가중 평균 값 필터링을 수행하시오.
# 마스크는 그림 4-7의 3x3과 5x5 마스크를 사용하여 각각의 결과를 한 화면에 출력하고, 원본 이미지와 비교하시오.
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

# 이미지 출력 함수
def image_print(img, title, print_num, current_num):
    print(print_num[0])
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')

lena = misc.imread('image/lena_256.bmp')

Weighted_Filter1=np.array([[1,2,1],[2,4,2],[1,2,1]])
Weighted_Filter1=Weighted_Filter1/np.sum(Weighted_Filter1)

Weighted_Filter2=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[1,4,6,4,1],[4,16,24,16,4]])
Weighted_Filter2=Weighted_Filter2/np.sum(Weighted_Filter2)

Image_New1 = im_filtering(lena, Weighted_Filter1, 3)
Image_New2 = im_filtering(lena, Weighted_Filter2, 5)

image_print(lena,"lena",(1,3),1)
image_print(Image_New1,"3X3",(1,3),2)
image_print(Image_New2,"5X5",(1,3),3)

plt.show()