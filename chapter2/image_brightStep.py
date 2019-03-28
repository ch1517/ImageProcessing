import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
# im_new = np.ones() 1로 채운다
# im_new = np.zeros(row,col) 0으로 채운다

N1=100
N2=150
N3=200
im_new = np.ndarray(shape=(row,col),dtype=np.uint8) # 이미지 처리 배열
for y in range(row):
    for x in range(col):
        value = im[y,x]
        if value > 0 and value < N1 :
            im_new[y,x] = 0;
        elif value > N1 and value < N2 :
            im_new[y,x] = N1;
        elif value > N2 and value < N3 :
            im_new[y,x] = N2;
        else:
            im_new[y,x] = N3;

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("mean")
plt.gray()
plt.imshow(im_new)
plt.axis('off')

plt.show()