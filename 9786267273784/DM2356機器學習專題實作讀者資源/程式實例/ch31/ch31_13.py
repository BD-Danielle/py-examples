# ch31_13.py
import pandas as pd
import numpy as np

df = pd.read_csv('Mall_Customers.csv')

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

# 統計數據概述
print(f"數據概述\n{df.describe()}")



