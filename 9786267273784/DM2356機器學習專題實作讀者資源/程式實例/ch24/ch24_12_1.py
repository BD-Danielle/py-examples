# ch24_12_1.py
import pandas as pd
import matplotlib.pyplot as plt

# 讀取數據
df = pd.read_csv('diabetes_new.csv')

# 定義中文標題
titles = ['懷孕次數', '血糖值', '血壓', '皮膚厚度', '胰島素',
          'BMI', '糖尿病家族函數', '年齡', '是否有糖尿病']

# 建立一個新的 figure，並設定其大小
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig = plt.figure(figsize=(15, 10))

# 為每個特徵繪製一個子圖
for i, col in enumerate(df.columns, 1):      # 包含 'Outcome'
    ax = fig.add_subplot(3, 3, i)
    df[col].hist(bins=10, ax=ax)
    ax.set_title(titles[i-1], fontsize=14)

# 顯示圖形
plt.subplots_adjust(wspace=0.3, hspace=0.5)  # 調整子圖間的間距
plt.show()



