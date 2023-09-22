# ch31_17.py
import pandas as pd
import numpy as np

df = pd.read_csv('wine_reviews.csv')

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

# 使用 drop 方法來刪除第一欄
df = df.drop(df.columns[0], axis=1)

# 輸出數據概述
print(f"數據概述\n{df.describe()}")



