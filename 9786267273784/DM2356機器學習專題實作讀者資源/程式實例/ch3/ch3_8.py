# ch3_8.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 取得測試資料
x = np.arange(start=-4,stop=5)
y = np.arange(start=-4,stop=5)
X, Y = np.meshgrid(x,y)
# 建立子圖
Z = X + Y
fig,ax = plt.subplots(subplot_kw={'projection':'3d'})
# 繪製 3D 網格圖
ax.scatter(X, Y, Z, color='b')              # 繪點  
ax.plot_wireframe(X, Y, Z, color='g')       # 繪網格線

ax.set_title('繪製 3D 網格圖',fontsize=16,color='b')
ax.set_xlabel('X軸',color='b')
ax.set_ylabel('Y軸',color='b')
ax.set_zlabel('Z軸',color='b')
plt.show()



      
