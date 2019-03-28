# 3-4 영상의 뺄셈
# h(x,y)=|f(x,y)-g(x,y)|
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

diff1=misc.imread('image/diff1.bmp')
diff2=misc.imread('image/diff2.bmp')

diff1_1 = np.float32(diff1)
diff2_1 = np.float32(diff2)

im_new = np.uint8(np.where(diff1_1-diff2_1<0,0,diff1_1-diff2_1))

im_new = abs(im_new)

plt.subplot(1,3,1), plt.imshow(diff1), plt.gray(), plt.title('Image1'), plt.axis('off')
plt.subplot(1,3,2), plt.imshow(diff2), plt.gray(), plt.title('Image2'), plt.axis('off')
plt.subplot(1,3,3), plt.imshow(im_new), plt.gray(), plt.title('difference Image'), plt.axis('off')
plt.show()