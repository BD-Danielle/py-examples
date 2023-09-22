# ch23_13.py
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target          # 加上目標欄位的房價欄位

# 建立一個含有兩個子圖的畫布，這裡 nrows=1, ncols=2
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# 在第一個子圖繪製 低收入比例 vs 房價
axs[0].scatter(df['LSTAT'],df['MEDV'])
axs[0].set_xlabel('低收入比例')
axs[0].set_ylabel('房價')
axs[0].set_title('低收入比例 vs 房價') 

# 在第二個子圖繪製 房間數 vs 房價
axs[1].scatter(df['RM'],df['MEDV'])
axs[1].set_xlabel('房間數')
axs[1].set_ylabel('房價')
axs[1].set_title('房間數 vs 房價')

# 自動調整子圖間距
plt.tight_layout()
plt.show()



