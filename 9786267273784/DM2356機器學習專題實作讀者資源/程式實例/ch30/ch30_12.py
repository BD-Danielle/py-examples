# ch30_12.py
import pandas as pd
import numpy as np

df = pd.read_csv('glass.csv')
pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

# 顯示前 5 筆數據
print(df.head())
print('-'*70)

# 顯示數據集的大小
print(f"數據集外形 : {df.shape}")
print('-'*70)

# 查看各特徵的數據類型和非空值的數量
print("數據類型和非空值的數量")
print(df.info())
print('-'*70)

# 統計數據概述, 排除 'Type' 特徵
df_without_type = df.drop('Type', axis=1)
print(f"數據概述\n{df_without_type.describe()}")



