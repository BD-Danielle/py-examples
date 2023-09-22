# ch32_3_2.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 載入Iris數據集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 標準化特徵
sc = StandardScaler()
X_std = sc.fit_transform(X)

# 使用PCA降維
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)

print(f"輸出主成份\n{pca.components_}")

# 繪製熱圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號
plt.figure(figsize=(10, 5))
sns.heatmap(pca.components_,
            cmap='viridis',
            yticklabels=['PCA Component 1', 'PCA Component 2'],
            xticklabels=iris.feature_names,
            cbar=True,
            annot=True)
plt.title('原始特徵與主成份相關係數熱圖')
plt.show()


