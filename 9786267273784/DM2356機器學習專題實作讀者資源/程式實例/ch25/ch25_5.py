# ch25_5.py
import seaborn as sns
import pandas as pd

# 設置pandas的顯示選項以便可以看到所有列
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)         # 設定顯示寬度

# 加載鐵達尼號數據集
titanic = sns.load_dataset('titanic')

# 查看數據集的一些基本欄位資料
print(titanic.info())
print('-'*75)

# 查看數據集的統計資料
print(titanic.describe())
print('-'*75)

# 顯示前 5 行數據
print(titanic.head())
