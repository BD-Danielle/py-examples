# ch27_12.py
from sklearn.datasets import load_iris
import pandas as pd

# 載入鳶尾花數據集
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# 將數字標籤轉換為文字標籤
df['species'] = df['species'].map({0:'setosa',1:'versicolor',2:'virginica'})
print(df.head())
print(df.groupby('species').size())










