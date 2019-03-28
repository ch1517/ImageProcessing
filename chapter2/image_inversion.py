# 가. 영상 반전하기
# g(x,y)=255-f(x,y)
from scipy import misc
import matplotlib.pyplot as plt

im = misc.imread('image/lena_256.bmp')
row, col = im.shape
# for y in range(row):
#     for x in range(col):
#         g[y,x] = 255-im[y,x]
im_inversion = 255-im

plt.subplot(1,2,1);
plt.title("original")
plt.gray()
plt.imshow(im)
plt.axis('off')

plt.subplot(1,2,2);
plt.title("inversion")
plt.gray()
plt.imshow(im_inversion)
plt.axis('off')

plt.show()