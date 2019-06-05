# 1. lena 영상을 이용하여 평균 값 필터링을 수행하시오. 마스크는 3*3, 5*5. 7*7, 9*9, 11*11을 사용하여
# 각각의 결과를 한 화면에 출력하고, 원본 이미지와 비교하시오.
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

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

def make_filter(num):
    Identity_Filter = np.ones(shape=(num,num))
    Identity_Filter/=np.sum(Identity_Filter)
    return Identity_Filter

# 이미지 출력 함수
def image_print(img, title, print_num, current_num):
    print(print_num[0])
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')

lena = misc.imread('image/lena_256.bmp')
Image3 = im_filtering(lena, make_filter(3), 3)
Image5 = im_filtering(lena, make_filter(5), 5)
Image7 = im_filtering(lena, make_filter(7), 7)
Image9 = im_filtering(lena, make_filter(9), 9)
Image11 = im_filtering(lena, make_filter(11), 11)

print_num = [2,3]
image_print(lena, "lena",  print_num, 1)
image_print(Image3, "3X3", print_num, 2)
image_print(Image5, "5X5",  print_num, 3)
image_print(Image7, "7X7", print_num, 4)
image_print(Image9, "9X9", print_num, 5)
image_print(Image11, "11X11", print_num, 6)

plt.show()
