# ch23_12.py
import pandas as pd
from sklearn import datasets

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target          # 加上目標欄位的房價欄位
# 挑出最相關的 3 個索引
print(df.corr().abs().nlargest(3,'MEDV').index)
# 輸出最相關的 3 個值
print(df.corr().abs().nlargest(3,'MEDV').values[:,13])



