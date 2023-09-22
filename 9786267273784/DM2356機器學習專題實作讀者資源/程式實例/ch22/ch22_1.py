# ch22_1.py
from sklearn.datasets import make_regression

# 生成線性數據
X, y = make_regression(n_features=1, noise=0, random_state=10)

# 輸出 X 的資料格式
print("輸出 X 的資料格式 :")
print(type(X))
print(f"陣列維度 = {X.ndim}")
print(f"陣列外型 = {X.shape}")
print(f"陣列大小 = {X.size}")
# 輸出前 5 個 X1 的樣本
print("前 5 個 X 的樣本 :")
print(X[:5])
print("="*70)

# 輸出 y 的資料格式
print("輸出 y 的資料格式 :")
print(type(y))
print(f"陣列維度 = {y.ndim}")
print(f"陣列外型 = {y.shape}")
print(f"陣列大小 = {y.size}")
# 輸出前 5 個 y 的樣本
print("前 5 個 y 的樣本 :")
print(y[:5])



