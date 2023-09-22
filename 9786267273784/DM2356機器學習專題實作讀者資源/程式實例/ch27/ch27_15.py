# ch27_15.py
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

# 使用 seaborn 的 pairplot 函數繪製所有特徵的配對散點圖
sns.pairplot(df, hue='species')

plt.show()



