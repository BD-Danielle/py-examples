# ch25_9.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv') 

# 刪除客戶ID列, 因為它對我們的分析沒有幫助
df = df.drop(['customerID'], axis=1)

# 迴圈處理多個特徵, 使用 LabelEncoder 進行數值轉換
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

# 用刪除缺失值方式, 處理缺失數據
df = df.dropna()

# 輸出前 5 筆數據
print(df.head())


