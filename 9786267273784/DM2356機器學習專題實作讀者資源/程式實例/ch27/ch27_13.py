# ch27_13.py
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# 載入鳶尾花數據集
iris = load_iris()

# 將數據集轉換為 DataFrame 格式, 方便後續繪圖
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# 將數字標籤轉換為文字標籤
df['species'] = df['species'].map({0:'setosa',1: 'versicolor',2: 'virginica'})

# 用 seaborn 的 scatterplot()繪製散點圖, hue 參數表示按照哪個特徵進行顏色區分
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)',
                style='species', hue='species')

plt.title("花萼長度(sepal length) vs 花萼寬度(sepal width)")
plt.show()



