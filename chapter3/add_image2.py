# 3-2 영상의 덧셈
# h(x,y) = af(x,y)+(1-a)g(x,y)
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


im_new3 = np.zeros(shape=(256,256))

for i in range(1,9):
    filename = 'image/noise'+ str(i) +'.bmp'
    im = misc.imread(filename)
    plt.subplot(2,4,i),plt.imshow(im),plt.gray()
    plt.title('Noisy Image: %i'%(i)), plt.axis('off')
    im_new3 = im_new3+np.float32(im)
plt.show()

# 평균값 구하기
im_new3/=8

plt.imshow(im_new3), plt.gray(), plt.title('AVERAGE'), plt.axis('off')
plt.show()