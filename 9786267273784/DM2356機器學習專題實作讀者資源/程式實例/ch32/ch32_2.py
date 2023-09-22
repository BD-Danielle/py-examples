# ch32_2.py
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# 加載 iris 數據集
iris = load_iris()
X = iris.data
print(f"維度 = {len(X[0])}")
print(X[0])
print("-"*70)

# 建立 PCA 實例並指定要保留的主成分數量
pca = PCA(n_components=2)

# 對數據應用 PCA 降維, X_pca將變成 2 維
X_pca = pca.fit_transform(X)
print(f"維度 = {len(X_pca[0])}")
print(X_pca[0].round(2))

