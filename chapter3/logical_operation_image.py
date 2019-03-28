# 3-5 영상의 논리연산의 예
import numpy as np
from scipy import misc

lena=misc.imread('image/lena_256.bmp')
gray128=misc.imread('image/gray128.bmp')
gray127=misc.imread('image/gray127.bmp')

# logical_and = lena & gray128
# logical_or = lena | gray127

logical_and = np.bitwise_and(lena,gray128)
logical_or = np.bitwise_or(lena,gray127)
