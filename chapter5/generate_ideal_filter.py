# 이상적(Ideal) 저역 및 고역 필터 만들기
import os
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

lowpass = np.zeros(shape=(256,256),dtype=np.uint8)
highpass = np.ones(shape=(256,256),dtype=np.uint8)
print(lowpass)
cx=128
cy=128
for y in range(256):
    for x in range(256):
        d = np.sqrt(pow((x-cx),2)+pow((y-cy),2))
        if d<30:
            lowpass[y,x] = 1
            highpass[y,x] = 0
print(lowpass)
plt.subplot("121"), plt.imshow(lowpass), plt.gray(), plt.axis('off')
plt.subplot("122"), plt.imshow(highpass), plt.gray(), plt.axis('off')
plt.show()