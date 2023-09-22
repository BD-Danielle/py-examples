# ch23_5.py
import pandas as pd
from sklearn import datasets

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(df.head())



