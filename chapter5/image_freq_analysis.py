# 주파수 영역, 시간 영역 변환
import os
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

lena = misc.imread('image/lena_256.bmp')

# Apply Fourier Transform : FFT -> F(x,y) : 복소수
F=np.fft.fft2(lena)

Mag = np.abs(F)
Mag = np.fft.fftshift(Mag) #영상 돌리기
pha = np.angle(F)

# plt.subplot("121"), plt.imshow(np.log10(Mag+1)), plt.gray(), plt.axis('off')
# plt.subplot("122"), plt.imshow(pha), plt.gray(), plt.axis('off')
# plt.show()

Mag = np.fft.fftshift(Mag) #영상 되돌리기
#|A|e&^jp
MakeComplex = Mag*np.exp(pha*1j)
IM = np.fft.ifft2(MakeComplex)
IM = np.real(IM)

plt.subplot("121"), plt.imshow(lena), plt.gray(), plt.axis('off')
plt.subplot("122"), plt.imshow(IM), plt.gray(), plt.axis('off')
plt.show()
