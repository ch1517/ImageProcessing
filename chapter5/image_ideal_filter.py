# 버터워스 필터 (Butterworth Filter)
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
#Make Filter
col = 256
row = 256
Low_Mask = np.zeros(shape=[row, col], dtype=np.float32)
High_Mask = np.zeros(shape=[row, col], dtype=np.float32)
BP_Mask = np.zeros(shape=[row, col], dtype=np.float32)
BS_Mask = np.zeros(shape=[row, col], dtype=np.float32)
Radius1 = 30
Radius2 = 60
cx = 128
cy = 128
for y in range(col):
    for x in range(row):
        dist = np.sqrt((cx-x)**2 + (cy-y)**2)
        if dist > Radius1:
            Low_Mask[x,y] = 0
            High_Mask[x,y] = 1
        else:
            Low_Mask[x,y] = 1
            High_Mask[x,y] = 0
for y in range(col):
    for x in range(row):
        dist = np.sqrt((cx-x)**2 + (cy-y)**2)
        if dist > Radius1 and dist < Radius2:
            BP_Mask[x,y] = 1
            BS_Mask[x,y] = 0
        else:
            BP_Mask[x,y] = 0
            BS_Mask[x,y] = 1
plt.subplot(221), plt.imshow(Low_Mask), plt.gray(), plt.axis('off'), plt.title('Ideal Lowpass')
plt.subplot(222), plt.imshow(High_Mask), plt.gray(), plt.axis('off'), plt.title('Ideal Highpass')
plt.subplot(223), plt.imshow(BP_Mask), plt.gray(), plt.axis('off'), plt.title('Ideal Bandpass')
plt.subplot(224), plt.imshow(BS_Mask), plt.gray(), plt.axis('off'), plt.title('Ideal Bandstop')
plt.show()