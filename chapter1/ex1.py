# 1.'lena256.bmp', 'lena_copy' 영상을 동시에 가로로 나열하여 출력하시오. 제목을 붙이고 axis의 ON/OFF를 선택하시오.
from scipy import misc
import matplotlib.pyplot as plt #그래픽 관련 라이브러리

#Image Read
lena = misc.imread('./image/lena_256.bmp')
row, col = lena.shape  #읽어들인 영상의 행과 열 크기를 알아낸다.

misc.imsave('./image/lena_copy.bmp', lena)

lena_copy = misc.imread('./image/lena_copy.bmp')
print(row)
print(col)

plt.gray()
plt.subplot(1,2,1)
plt.imshow(lena)
plt.axis('off')
plt.title('Lena Image')

plt.gray()
plt.subplot(1,2,2)
plt.imshow(lena_copy)
plt.axis('off')
plt.title('Lena_Copy Image')


plt.show()

