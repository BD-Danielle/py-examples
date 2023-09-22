# ch27_14.py
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# 載入鳶尾花數據集
iris = load_iris()

# 將數據集轉換為 DataFrame 格式，方便後續繪圖
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# 將數字標籤轉換為文字標籤
df['species'] = df['species'].map({0:'setosa',1:'versicolor',2:'virginica'})

# 使用 seaborn 的 pairplot 函數繪製 sepal length 和petal length 兩個特徵的圖形
sns.pairplot(df, vars=['sepal length (cm)','petal length (cm)'],hue='species')

plt.show()





