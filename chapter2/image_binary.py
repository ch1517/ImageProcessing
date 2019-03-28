# 바. 이진화
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
# im_binary=np.where(im>127,255,0)
im_new = np.ndarray(shape=(row,col),dtype=np.uint8) # 이미지 처리 배열
n=127
for y in range(row):
    for x in range(col):
        value = im[y,x]
        if value > n :
            im_new[y,x] = 255;
        else:
            im_new[y,x] = 0;

# binary = np.where(im>n,255,0)

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("binary")
plt.gray()
plt.imshow(im_new)
plt.axis('off')

plt.show()