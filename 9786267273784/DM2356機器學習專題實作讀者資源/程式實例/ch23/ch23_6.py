# ch23_6.py
import pandas as pd
from sklearn import datasets

# 加載波士頓房價數據集
boston = datasets.load_boston()

pd.set_option('display.max_columns', None)  # 顯示所有欄位

df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(df.head())



