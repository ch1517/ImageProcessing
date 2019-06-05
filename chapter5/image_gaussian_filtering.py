# 주파수 영역에서 가우시안 저역 및 고역 필터링 적용
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
col = 256
row = 256
cx = 128
cy = 128
D0 = 15
Gaussian_L = np.zeros(shape=[col, row], dtype=np.float32)
Gaussian_H = np.zeros(shape=[col, row], dtype=np.float32)
for x in range(col):
    for y in range(row):
        D = np.sqrt((cx - x) ** 2 + (cy - y) ** 2)
        Gaussian_L[x, y] = np.exp(-D**2 / (2*D0**2) )
Gaussian_H = 1 - Gaussian_L

lena = misc.imread('image/lena_256.bmp')

# Apply Fourier Transform : FFT -> F(x,y) : 복소수
F=np.fft.fft2(lena)

Mag = np.abs(F)
Mag = np.fft.fftshift(Mag) #영상 돌리기
pha = np.angle(F)

Mag1 = Mag*Gaussian_L
Mag2 = Mag*Gaussian_H

Mag1 = np.fft.fftshift(Mag1) #영상 되돌리기
Mag2 = np.fft.fftshift(Mag2) #영상 되돌리기
#|A|e&^jp
MakeComplex1 = Mag1*np.exp(pha*1j)
MakeComplex2 = Mag2*np.exp(pha*1j)

lowpass_img = np.fft.ifft2(MakeComplex1)
lowpass_img = np.real(lowpass_img)

highpass_img = np.fft.ifft2(MakeComplex2)
highpass_img = np.real(highpass_img)

plt.subplot(221),plt.imshow(Gaussian_L), plt.gray(), plt.axis('off'), plt.title('Gaussian Lowpass')
plt.subplot(222),plt.imshow(Gaussian_H), plt.gray(), plt.axis('off'),plt.title('Gaussian Highpass')
plt.subplot(223),plt.imshow(lowpass_img), plt.gray(), plt.axis('off'), plt.title('Gaussian Lowpass Image')
plt.subplot(224),plt.imshow(highpass_img), plt.gray(), plt.axis('off'),plt.title('Gaussian Highpass Image')
plt.show()