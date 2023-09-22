# ch30_14.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

# 創建DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = data.target

# 顯示數據集的前5筆
print(f"輸出前 5 筆資料\n{df.head()}")
print('-'*70)

# 顯示數據集的描述性統計信息
print(f"統計資訊\n{df.describe()}")
print('-'*70)

# 顯示各特徵與目標變數的相關性
print("輸出個特徵與目標變數的相關係數")
print(df.corr()['Target'].sort_values(ascending=False))

# 設定子圖間的間距
plt.subplots_adjust(hspace = 0.5, wspace = 0.6)

# 顯示數據分佈的直方圖
house_hist = df.hist(bins=50, figsize=(12,10))
for ax in house_hist.ravel():
    ax.set_title(ax.get_title())    # 設定標題
    ax.set_xlabel("Value")          # 設定x軸標籤
    ax.set_ylabel("Frequency")      # 設定y軸標籤

plt.show()


