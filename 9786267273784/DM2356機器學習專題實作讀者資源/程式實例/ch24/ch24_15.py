# ch24_15.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取糖尿病數據集
df = pd.read_csv('diabetes.csv')

# 將特徵名稱改成對應的繁體中文
df.columns = ['懷孕次數', '血糖值', '血壓', '皮膚厚度',
              '胰島素', 'BMI', '糖尿病家族函數', '年齡',
              '是否有糖尿病']

# 繪製皮爾遜相關係數熱力圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.figure(figsize=(12,10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('糖尿病特徵皮爾遜相關係數熱力圖')
plt.yticks(rotation=30)          # 旋轉標籤文字
plt.show()






