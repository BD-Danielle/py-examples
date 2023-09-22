# ch3_9.py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False      # 負數符號
x = np.linspace(-5, 5, 30)                      # 設定 x 的值範圍
y = np.linspace(-5, 5, 30)                      # 設定 y 的值範圍
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))                # 計算函數的值
# 建立一個新的圖像
fig = plt.figure(figsize=(10, 6))
# 建立第 1 個子圖（3D 網格圖）
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_wireframe(X, Y, Z, linewidth=0.5, cmap='rainbow')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D 網格圖')
# 建立第 2 個子圖（3D 表面圖）
ax1 = fig.add_subplot(2, 2, 2, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='rainbow')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D 表面圖')
# 建立第 3 個子圖（等高線圖）
ax2 = fig.add_subplot(2, 2, 3)
contour = ax2.contour(X, Y, Z, cmap='rainbow')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('等高線圖')
fig.colorbar(contour)
# 建立第 4 個子圖（填充等高線圖）
ax2 = fig.add_subplot(2, 2, 4)
contour = ax2.contourf(X, Y, Z, cmap='rainbow')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('填充等高線圖')
fig.colorbar(contour)
# 顯示圖像
plt.subplots_adjust(wspace=0.4, hspace=0.4)     # 子圖的間距設定
plt.show()

