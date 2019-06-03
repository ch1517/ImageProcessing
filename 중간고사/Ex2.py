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

#평균 값 필터 만드는 함수
def make_filter(num):
    Identity_Filter = np.ones(shape=(num,num))
    Identity_Filter/=np.sum(Identity_Filter)
    return Identity_Filter

image_f = misc.imread('image/lena_256.bmp')
row, col = image_f.shape
image_g = im_filtering(image_f, make_filter(3), 3)
image_y = image_f+ (image_f-image_g)
# 이미지 출력 함수
def image_print(img, title, print_num, current_num):
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')

print_num = [1,2]
image_print(image_f, "InputImage",  print_num, 1)
image_print(image_y, "OutputImage",  print_num, 2)
plt.show()