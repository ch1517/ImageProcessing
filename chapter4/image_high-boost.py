# Unsharp mask 필터링에서 원본 영상의 화질을 더 보존하기 위한 High-boost 필터
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
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')
#a=0.8
Embossing_Filter1_1=np.array([[0,-1,0],[-1,4.8,-1],[0,-1,0]])
Embossing_Filter1_2=np.array([[-1,-1,-1],[-1,8.8,-1],[-1,-1,-1]])

#a=1.0
Embossing_Filter2_1=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
Embossing_Filter2_2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

#a=1.2
Embossing_Filter3_1=np.array([[0,-1,0],[-1,5.2,-1],[0,-1,0]])
Embossing_Filter3_2=np.array([[-1,-1,-1],[-1,9.2,-1],[-1,-1,-1]])

lena = misc.imread('image/medical.bmp')
Filter_Size = 3
Image_New1_1 = im_filtering(lena, Embossing_Filter1_1, Filter_Size)
Image_New1_2 = im_filtering(lena, Embossing_Filter1_2, Filter_Size)

Image_New2_1 = im_filtering(lena, Embossing_Filter2_1, Filter_Size)
Image_New2_2 = im_filtering(lena, Embossing_Filter2_2, Filter_Size)

Image_New3_1 = im_filtering(lena, Embossing_Filter3_1, Filter_Size)
Image_New3_2 = im_filtering(lena, Embossing_Filter3_2, Filter_Size)


print_num = [2,3]
image_print(Image_New1_1, "a=0.8",  print_num, 1)
image_print(Image_New1_2, "a=0.8",  print_num, 4)
image_print(Image_New2_1, "a=1.0",  print_num, 2)
image_print(Image_New2_2, "a=1.0",  print_num, 5)
image_print(Image_New3_1, "a=1.2",  print_num, 3)
image_print(Image_New3_2, "a=1.2",  print_num, 6)
plt.show()