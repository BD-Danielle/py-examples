# ch23_7.py
import pandas as pd
from sklearn import datasets

# 加載波士頓房價數據集
boston = datasets.load_boston()

pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(df.head())



