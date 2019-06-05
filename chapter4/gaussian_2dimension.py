# 3차원 가우시안 그래프 그리기
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

sigma = 10

g = np.zeros(shape=(256,256), dtype=np.float)
for y in range(-127,128):
    for x in range(-127,128):
        s=1/(2*np.pi*pow(sigma,2))
        v=-(pow(x,2)+pow(y,2))/(2*pow(sigma,2))
        g[y+127,x+127]=s*np.exp(v)

plt.imshow(g)
plt.gray()
plt.show() # 2차원 그래프로 그리기

from mpl_toolkits.mplot3d import Axes3D

sigma = 40

x=np.arange(-127,128,1.0)
y=np.arange(-127,128,1.0)
X,Y=np.meshgrid(x,y)

s=1/(2*np.pi*pow(sigma,2))
v=-(pow(X,2)+pow(Y,2))/(2*pow(sigma,2))
g=s*np.exp(v)

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,g)
plt.show() # 3차원 그래프로 그리기

#9*9 가우시안 필터
sigma = 1.0
g = np.zeros(shape=(9,9), dtype=np.float)
for y in range(-4,5):
    for x in range(-4,5):
        s=1/(2*np.pi*pow(sigma,2))
        v=-(pow(x,2)+pow(y,2))/(2*pow(sigma,2))
        g[y+4,x+4]=s*np.exp(v)
        print('{: .4f}' .format(g[y+4,x+4]), end=' ')
    print("")

plt.imshow(g)
plt.gray()
plt.show() # 2차원 그래프로 그리기

