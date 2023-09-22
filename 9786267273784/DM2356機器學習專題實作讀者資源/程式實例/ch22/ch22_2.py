# ch22_2.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號

# 生成兩組數據
X1, y1 = make_regression(n_features=1, noise=0, random_state=10)
X2, y2 = make_regression(n_features=1, noise=20, random_state=10)

# 建立一個含有兩個子圖的畫布，這裡 nrows=1, ncols=2 
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# 在第一個子圖繪製 noise 為 0 的數據
axs[0].scatter(X1, y1)
axs[0].set_title('Noise = 0')

# 在第二個子圖繪製 noise 為 20 的數據
axs[1].scatter(X2, y2)
axs[1].set_title('Noise = 20')

# 設置圖表標題和標籤
for ax in axs:
    ax.set_xlabel('特徵')
    ax.set_ylabel('目標')

# 自動調整子圖間距
plt.tight_layout()
plt.show()


