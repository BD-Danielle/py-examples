# ch26_5.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 讀取csv文件
data = pd.read_csv('adult.csv')
pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

# 數據清洗, 將'?'替換為 np.nan
data = data.replace('?', np.nan)
# 刪除包含缺失值的列(row)
data = data.dropna()
# 輸出前5筆資料
print(data.head())
print('-'*180)

# 將類別變數由文字轉換為數字, 使用LabelEncoder
le = LabelEncoder()
categorical_features = [i for i in data.columns if data.dtypes[i]=='object']
for col in categorical_features:
    data[col] = le.fit_transform(data[col])
print(data.head())

