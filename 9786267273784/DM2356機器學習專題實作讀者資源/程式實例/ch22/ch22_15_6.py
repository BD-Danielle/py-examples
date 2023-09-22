# ch22_15_6.py
import pandas as pd

# 建立一個包含類別數據的簡單數據集
data = {'color': ['red', 'blue', 'green', 'blue']}
df = pd.DataFrame(data)

# 使用pandas的get_dummies()方法進行one-hot編碼
encoded_df = pd.get_dummies(df, columns=['color'])

# 輸出結果
print(encoded_df)



