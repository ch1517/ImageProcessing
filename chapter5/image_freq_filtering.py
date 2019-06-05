# 주파수영역에서 저역 및 고역 필터링 적용
import os
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

lowpass = np.zeros(shape=(256,256),dtype=np.uint8)
highpass = np.ones(shape=(256,256),dtype=np.uint8)

cx=128
cy=128
for y in range(256):
    for x in range(256):
        d = np.sqrt(pow((x-cx),2)+pow((y-cy),2))
        if d<50:
            lowpass[y,x] = 1
            highpass[y,x] = 0

lena = misc.imread('image/lena_256.bmp')
# Apply Fourier Transform : FFT -> F(x,y) : 복소수
F=np.fft.fft2(lena)

Mag = np.abs(F)
Mag = np.fft.fftshift(Mag) #영상 돌리기
pha = np.angle(F)

Mag1 = Mag*lowpass
Mag2 = Mag*highpass

Mag1 = np.fft.fftshift(Mag1) #영상 되돌리기
Mag2 = np.fft.fftshift(Mag2) #영상 되돌리기
#|A|e&^jp
MakeComplex1 = Mag1*np.exp(pha*1j)
MakeComplex2 = Mag2*np.exp(pha*1j)

lowpass_img = np.fft.ifft2(MakeComplex1)
lowpass_img = np.real(lowpass_img)

highpass_img = np.fft.ifft2(MakeComplex2)
highpass_img = np.real(highpass_img)

plt.subplot("131"), plt.imshow(lena), plt.gray(), plt.axis('off'), plt.title("original")
plt.subplot("132"), plt.imshow(lowpass_img), plt.gray(), plt.axis('off'), plt.title("lowPass")
plt.subplot("133"), plt.imshow(highpass_img), plt.gray(), plt.axis('off'), plt.title("highPass")
plt.show()