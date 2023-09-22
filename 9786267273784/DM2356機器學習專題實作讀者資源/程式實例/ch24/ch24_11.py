# ch24_11.py
import pandas as pd

# 讀取數據
df = pd.read_csv('diabetes.csv')

# 設定可能存在缺失值的特徵
columns_with_potential_missing_values = ['Glucose', 'BloodPressure',
                       'SkinThickness', 'Insulin', 'BMI']

# 將可能存在缺失值的特徵中的0值替換為該特徵的中位數
for column in columns_with_potential_missing_values:
    median = df[column].median()
    df[column] = df[column].replace(to_replace=0, value=median)

# 將處理過的數據存入新的CSV檔案
df.to_csv('diabetes_new.csv', index=False)
