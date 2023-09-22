# ch28_20.py
import pandas as pd

# 讀取數據集
df = pd.read_csv('auto-mpg.csv')

pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

# 顯示數據集的前5行
print(df.head())

# 顯示數據集的筆數
print(f'這個數據共有 {df.shape[0]} 筆數')
