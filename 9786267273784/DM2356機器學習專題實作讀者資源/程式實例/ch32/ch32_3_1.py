# ch32_3_1.py
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 載入 Iris 數據集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 標準化特徵
sc = StandardScaler()
X_std = sc.fit_transform(X)

# 使用PCA降維
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)

# 建立子圖
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# 繪製原始特徵散點圖
for target, color in zip(range(3), ['r', 'b', 'g']):
    ax[0].scatter(X_std[y == target, 0], X_std[y == target, 1], color=color,
                  alpha=0.5, label=iris.target_names[target])
ax[0].set_xlabel('Sepal Length')
ax[0].set_ylabel('Sepal Width')
ax[0].legend()
ax[0].set_title('Original Features Scatter Plot')

# 繪製 PCA 主成分散點圖
for target, color in zip(range(3), ['r', 'b', 'g']):
    ax[1].scatter(X_pca[y == target, 0], X_pca[y == target, 1], color=color,
                  alpha=0.5, label=iris.target_names[target])
ax[1].set_xlabel('PCA Component 1')
ax[1].set_ylabel('PCA Component 2')
ax[1].legend()
ax[1].set_title('PCA Components Scatter Plot')

plt.show()
