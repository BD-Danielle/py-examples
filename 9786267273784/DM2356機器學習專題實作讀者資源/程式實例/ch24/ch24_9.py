# ch24_9.py
import pandas as pd

# 讀取和輸出糖尿病數據集
df = pd.read_csv('diabetes.csv')
pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度
print(df.head())                            # 前 5 筆資料
print('-'*70)

# 設定輸出到小數第 2 位
pd.set_option('display.float_format', '{:.2f}'.format)
print('輸出數據集的統計資訊')
print(df.describe())                        





