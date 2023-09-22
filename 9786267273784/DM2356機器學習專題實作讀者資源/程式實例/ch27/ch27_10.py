# ch27_10.py
import pandas as pd
from sklearn import datasets

# 加載鳶尾花數據集
iris = datasets.load_iris()

pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Species'] = iris.target     # 加上目標欄位的鳶尾花標記
print(df.head())



