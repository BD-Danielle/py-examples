# ch23_23.py
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
X = pd.DataFrame(np.c_[df['LSTAT'],df['RM']], columns=['LSTAT','RM'])
Y = boston.target

# 將數據分為訓練集和測試集（這裡使用80-20的比例）
X_train, X_test, Y_train, Y_test = \
         train_test_split(X, Y, test_size=0.2, random_state=1)

# 使用 PolynomialFeatures 生成二元二次多項式特徵
degree = 2                      
poly = PolynomialFeatures(degree)
X_train_poly = poly.fit_transform(X_train)

# 擬合訓練集數據建立二元二次多項式迴歸模型
model = LinearRegression()
model.fit(X_train_poly, Y_train)

# 用測試資料計算模型的性能指標
X_test_poly = poly.fit_transform(X_test)
print(f"測試數據R-squared Score:{model.score(X_test_poly, Y_test)}")

# 查看模型的截距和係數
intercept = model.intercept_
coeff = model.coef_
print(f"截距 (b0)    : {intercept:.3f}")
print(poly.get_feature_names_out())    # 二元二次的多項式特徵
print(f"係數 (b0, b1, b2, b3, b4, b5, b6): {coeff}")




