# 소금-후추 잡음 제거하는 mdedian filering
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
def noisy(noise_typ,image):
    if noise_typ == "gauss":
        row, col = image.shape
        mean = 0
        var = 0.5
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col))
        gauss = gauss.reshape(row,col)
        noisy = image + 10.0*gauss
        return noisy
    elif noise_typ == "s&p":
        row,col = image.shape
        s_vs_p = 0.5
        amount = 0.2
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 255
        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * 10.0*vals) / float(vals)
        return noisy
    elif noise_typ =="speckle":
        row,col = image.shape
        gauss = np.random.randn(row,col)
        gauss = gauss.reshape(row,col)
        noisy = image + image * 0.1*gauss
        return noisy

def Median_filtering(im, FilterSize):
    row, col = im.shape
    padding=int(FilterSize/2)
    Image_Buffer = np.zeros(shape=(row+2*padding,col+2*padding), dtype=np.uint8)
    Image_Buffer[padding:row+padding, padding:col+padding] = im[:,:]
    Image_New = np.zeros(shape=(row,col), dtype=np.uint8)
    for y in range(padding,row+padding):
        for x in range(padding,col+padding):
            buff = Image_Buffer[y-padding:y+padding+1,x-padding:x+padding+1]
            tmp = np.sort(buff,axis=None)
            Image_New[y-padding,x-padding] = tmp[4]
    return Image_New
# 이미지 출력 함수
def image_print(img, title, print_num, current_num):
    plt.subplot(print_num[0],print_num[1],current_num)
    plt.title(title)
    plt.gray()
    plt.imshow(img)
    plt.axis('off')

lena = misc.imread('image/lena_256.bmp')
row, col = lena.shape

sandp = noisy("s&p",lena)

print_num = [1,3]
FilterSize = 3
# Image_New1 = im_filtering(gauss, Weighted_Filter, FilterSize)
# Image_New2 = im_filtering(sandp, Weighted_Filter, FilterSize)
Image_New3 =  Median_filtering(sandp,FilterSize) #median_filter

image_print(lena, "lena",  print_num, 1)
# image_print(gauss, "gauss", print_num, 2)
# image_print(Image_New2, "mean_filter", print_num, 3)

image_print(sandp, "s&p", print_num, 2)
image_print(Image_New3, "median_filter", print_num, 3)
plt.show()