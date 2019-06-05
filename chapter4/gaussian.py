# 공식을 이용한 가우시안 그래프 그리기
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from scipy import ndimage

sigma = 50.0
g = np.zeros(shape=(256), dtype=np.float)
for x in range(-127,129):
    s=np.sqrt(2*np.pi)*sigma
    v=-pow(x,2)/(2*pow(sigma,2))
    g[x+127]=s*np.exp(v)

plt.plot(g)
plt.show()

sigma = 50.0
x = np.arange(-127,128)
s=np.sqrt(2*np.pi)*sigma
v=-pow(x,2)/(2*pow(sigma,2))
g=s*np.exp(v)

plt.plot(g)
plt.show()