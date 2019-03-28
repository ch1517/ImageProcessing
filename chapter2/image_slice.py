# 사. 슬라이스
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
# im_binary=np.where(im>127,255,0)
im_new = np.ndarray(shape=(row,col),dtype=np.uint8) # 이미지 처리 배열
N1=100
N2=150
for y in range(row):
    for x in range(col):
        value = im[y,x]
        if value > N1 and value < N2:
            im_new[y,x] = 255;
        else:
            im_new[y,x] = value;

slice = np.where(im>N1,np.where(im<N2,255,im),im)

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("slice")
plt.gray()
plt.imshow(slice)
plt.axis('off')

plt.show()