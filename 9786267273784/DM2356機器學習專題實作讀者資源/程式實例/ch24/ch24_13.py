# ch24_13.py
import pandas as pd
import matplotlib.pyplot as plt

# 讀取數據
df = pd.read_csv('diabetes_new.csv')

# 將英文欄位名稱轉換為中文
df.columns = ['懷孕次數','血糖值','血壓','皮膚厚度',
              '胰島素','BMI','糖尿病家族函數','年齡',
              '是否有糖尿病']

# 使用 pandas 的 boxplot() 方法繪製箱形圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.figure(figsize=(12,8)) # 設定圖形大小
df.boxplot() # 繪製箱形圖

# 顯示標題並設定字體大小
plt.title('糖尿病數據特徵箱形圖', fontsize=20)

# 設定 x 軸和 y 軸的標籤
plt.xlabel('糖尿病數據特徵欄位', fontsize=15)
plt.ylabel('數值', fontsize=15)

# 旋轉 x 軸的標籤，使其更易讀
plt.xticks(rotation=30, ha='right')
plt.show()


