# ch28_15_1.py
from sklearn.datasets import load_breast_cancer
import pandas as pd

# 載入 breast_cancer 數據集
data = load_breast_cancer()

# 建立一個 DataFrame 來展示數據
df = pd.DataFrame(data.data, columns=data.feature_names)

# 輸出數據的形狀（樣本數和特徵數）
print(f"數據外形 : {df.shape}")

# 輸出前 5 筆數據
print(f"前 5 筆資料 :\n{df.head()}")

# 輸出特徵名稱
print(f"特徵名稱 :\n{data.feature_names}")

# 輸出目標名稱（標籤名稱）
print(f"目標標籤 : {data.target_names}")




