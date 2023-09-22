# ch24_10.py
import pandas as pd

# 讀取糖尿病數據集
df = pd.read_csv('diabetes.csv')

# 檢查是否有缺失值
print(df.isnull().sum())

