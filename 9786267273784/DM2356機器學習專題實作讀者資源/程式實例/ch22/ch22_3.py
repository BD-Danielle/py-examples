# ch22_3.py
from sklearn.datasets import make_blobs

# 生成數據集
X, y = make_blobs(n_samples=500,n_features=2,centers=5,random_state=1)
# 輸出 X1 的資料格式
print("輸出 X 的資料格式 :")
print(type(X))

# 輸出前 5 個 X1 的樣本
print("前 5 個 X 的樣本 :")
print(X[:5])
print("="*70)

# 二維陣列切片輸出前 5 個 X[:,0], 結果是降維度索引 0 的一維陣列
print("前 5 個 X[:,0] 的樣本 :")
xx = X[:5]
print(xx[:,0])
print("="*70)

# 二維陣列切片輸出前 5 個 X[:,1], 結果是降維度索引 1 的一維陣列
print("前 5 個 X[:,1] 的樣本 :")
print(xx[:,1])
print("="*70)

# 輸出前 5 個 y 的樣本
print("前 5 個 y 的樣本 :")
print(y[:5])



