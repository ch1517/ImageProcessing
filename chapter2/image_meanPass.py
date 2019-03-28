# 차. 중간통과
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
N1=100
N2=150

# im_new = np.ones() 1로 채운다
# im_new = np.zeros(row,col) 0으로 채운다

im_new = np.ndarray(shape=(row,col),dtype=np.uint8) # 이미지 처리 배열
for y in range(row):
    for x in range(col):
        value = im[y,x]
        if value > N1 and value < N2 :
            im_new[y,x] = 0
        else:
            im_new[y,x] = value

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("pass")
plt.gray()
plt.imshow(im_new)
plt.axis('off')

plt.show()