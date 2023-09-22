# ch33_8.py
import pandas as pd

# 讀取數據並更改欄位名稱
data = pd.read_csv('OldFaithful.txt', sep="\s+", skiprows=1,
                   names=['Dropped', 'Waiting', 'Eruptions'])

# 拋棄不需要的欄位
data = data.drop(['Dropped'], axis=1)

# 存儲數據
data.to_csv('oldfaithful.csv', index=False)
print("成功將數據存儲到 oldfaithful.csv 文件中!")



