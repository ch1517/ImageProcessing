#버터워스 필터 (Butterworth Filter)
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
col = 256
row = 256
cx = 128
cy = 128
D0 = 50 # 원의 크기
N = 2 # 필터링 정도
W = 30 #링의 두께
BW_L = np.zeros(shape=[col,row], dtype=np.float32)
BW_H = np.zeros(shape=[col,row], dtype=np.float32)
BW_BP = np.zeros(shape=[col,row], dtype=np.float32)
BW_BS = np.zeros(shape=[col,row], dtype=np.float32)
for x in range(col):
    for y in range(row):
        D = np.sqrt((cx-x)**2 + (cy-y)**2)
        s = (W * D) / (D ** 2 - D0 ** 2)
        BW_L[x, y] = 1 / (1 + pow(D/D0, 2*N ))
        BW_H[x, y] = 1 / (1 + pow(D0/D, 2*N ))
        BW_BS[x, y] = 1 / (1 + pow(s, 2*N ))
BW_BP = 1 - BW_BS
plt.subplot(221), plt.imshow(BW_L), plt.gray(), plt.axis('off'), plt.title('Butterworth Lowpass')
plt.subplot(222), plt.imshow(BW_H), plt.gray(), plt.axis('off'), plt.title('Butterworth Highpass')
plt.subplot(223), plt.imshow(BW_BP), plt.gray(), plt.axis('off'), plt.title('Butterworth Bandpass')
plt.subplot(224), plt.imshow(BW_BS), plt.gray(), plt.axis('off'), plt.title('Butterworth Bandstop')
plt.show()