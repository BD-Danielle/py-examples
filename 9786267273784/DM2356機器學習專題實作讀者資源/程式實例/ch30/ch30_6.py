# ch30_6.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('insurance.csv')
# 顯示各變數的直方圖
df.hist(figsize=(10,10))
plt.show()

# 使用seaborn畫出各個變數間的關係
sns.pairplot(df)
plt.show()

# 畫出相關性熱力圖
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGn')
plt.show()




