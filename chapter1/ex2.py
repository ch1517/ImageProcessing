# 2. 인터넷 검색 등을 통해 6장의 사진을 찾아 이들 6장의 영상을 동시에 출력하시오.
from scipy import misc
import matplotlib.pyplot as plt #그래픽 관련 라이브러리
#Image Read
for i  in range (1,7):
    oo = misc.imread('./image/'+repr(i)+'.jpg')
    plt.subplot(1,6,i)
    plt.imshow(oo)
    plt.axis('off')
    plt.title(repr(i))

plt.show()