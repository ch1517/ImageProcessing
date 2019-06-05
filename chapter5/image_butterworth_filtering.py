# butterworth_filter 를 이용한 이미지 필터링
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
col = 256
row = 256
cx = 128
cy = 128
D0 = 50 # 원의 크기
N = 1 # 필터링 정도
W = 20 #링의 두께
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

#필터링
lena = misc.imread('image/lena_256.bmp')

# Apply Fourier Transform : FFT -> F(x,y) : 복소수
F=np.fft.fft2(lena)

Mag = np.abs(F)
Mag = np.fft.fftshift(Mag) #영상 돌리기
pha = np.angle(F)

Mag_L = Mag*BW_L
Mag_H = Mag*BW_H
Mag_BP = Mag*BW_BP
Mag_BS = Mag*BW_BS

Mag_L = np.fft.fftshift(Mag_L) #영상 되돌리기
Mag_H = np.fft.fftshift(Mag_H) #영상 되돌리기
Mag_BP = np.fft.fftshift(Mag_BP) #영상 되돌리기
Mag_BS = np.fft.fftshift(Mag_BS) #영상 되돌리기

#|A|e&^jp
MakeComplex1 = Mag_L*np.exp(pha*1j)
MakeComplex2 = Mag_H*np.exp(pha*1j)
MakeComplex3 = Mag_BP*np.exp(pha*1j)
MakeComplex4 = Mag_BS*np.exp(pha*1j)

lowpass_img = np.fft.ifft2(MakeComplex1)
lowpass_img = np.real(lowpass_img)

highpass_img = np.fft.ifft2(MakeComplex2)
highpass_img = np.real(highpass_img)

bandpass_img = np.fft.ifft2(MakeComplex3)
bandpass_img = np.real(bandpass_img)

bandstop_img = np.fft.ifft2(MakeComplex4)
bandstop_img = np.real(bandstop_img)


plt.subplot(241), plt.imshow(BW_L), plt.gray(), plt.axis('off'), plt.title('Butterworth Lowpass')
plt.subplot(242), plt.imshow(BW_H), plt.gray(), plt.axis('off'), plt.title('Butterworth Highpass')
plt.subplot(243), plt.imshow(BW_BP), plt.gray(), plt.axis('off'), plt.title('Butterworth Bandpass')
plt.subplot(244), plt.imshow(BW_BS), plt.gray(), plt.axis('off'), plt.title('Butterworth Bandstop')

plt.subplot(245), plt.imshow(lowpass_img), plt.gray(), plt.axis('off'), plt.title('Lowpass Image')
plt.subplot(246), plt.imshow(highpass_img), plt.gray(), plt.axis('off'), plt.title('Highpass Image')
plt.subplot(247), plt.imshow(bandpass_img), plt.gray(), plt.axis('off'), plt.title('Bandpass Image')
plt.subplot(248), plt.imshow(bandstop_img), plt.gray(), plt.axis('off'), plt.title('Bandstop Image')
plt.show()