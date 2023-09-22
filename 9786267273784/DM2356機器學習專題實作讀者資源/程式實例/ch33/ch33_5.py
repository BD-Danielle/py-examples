# ch33_5.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度
pd.set_option('display.unicode.east_asian_width', True)
data = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)
data.columns = ['面積', '周長', '粗造度', '長度',
                '寬度', '不對稱係數', '長度比', '分類']

# 輸出前 5 筆數據
print(data.head())

# 使用描述方法獲得數據的統計信息
print(data.describe())

# 複製原始數據, 刪除 '分類' 特徵, 防止影響後續操作
data_without_class = data.copy()
data_without_class = data_without_class.drop('分類', axis=1)

# 使用箱形圖查看每個特徵的分佈
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.figure(figsize=(12, 6))
sns.boxplot(data=data_without_class)
plt.title('特徵分佈的箱形圖')
plt.show()

# 使用散點圖矩陣查看配對特徵之間的關係
sns.pairplot(data, hue='分類')
plt.show()
