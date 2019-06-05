#butterworth low,high,bandpass,pandstop 3D로 그리기
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage
from mpl_toolkits.mplot3d import Axes3D
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


x=np.arange(0,col,1.0)
y=np.arange(0,row,1.0)
fig = plt.figure()								# 이건 꼭 입력해야한다.

X, Y = np.meshgrid(x, y)  # create the "base grid"
D = np.sqrt((cx-X)**2 + (cy-Y)**2)
s = (W * D) / (D ** 2 - D0 ** 2)
BW_L = 1 / (1 + pow(D/D0, 2*N ))
BW_H = 1 / (1 + pow(D0/D, 2*N ))
BW_BS = 1 / (1 + pow(s, 2*N ))
BW_BP = 1 - BW_BS

ax1 = fig.add_subplot( 2 , 2 , 1 , projection = '3d' )
ax1.plot_surface(X,Y,BW_L)
ax1.set_title("BL")

ax2 = fig.add_subplot ( 2 , 2 , 2 , projection = '3d' )
ax2.plot_surface(X,Y,BW_H)
ax2.set_title("BH")

ax3 = fig.add_subplot ( 2 , 2 , 3 , projection = '3d' )
ax3.plot_surface(X,Y,BW_BP)
ax3.set_title("BBP")

ax4 = fig.add_subplot ( 2 , 2 , 4 , projection = '3d' )
ax4.plot_surface(X,Y,BW_BS)
ax4.set_title("BBS")

plt.tight_layout()
plt.show() # 3차원 그래프로 그리기
