# ch23_20.py
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# 創建原始的 'x' 特徵
X = np.array([[1], [2], [3], [4]])

# 使用 PolynomialFeatures 生成一元二次多項式特徵
degree = 2                          # 設定生成二次多項式
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

# 列印生成的多項式特徵
print(poly.get_feature_names_out(input_features=['x']))
print(X_poly)



