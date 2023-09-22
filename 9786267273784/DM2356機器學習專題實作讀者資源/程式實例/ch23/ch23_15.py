# ch23_15.py
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from joblib import dump

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
X = pd.DataFrame(np.c_[df['LSTAT'],df['RM']], columns=['LSTAT','RM'])
Y = boston.target


# 將數據分為訓練集和測試集（這裡使用80-20的比例）
X_train, X_test, Y_train, Y_test = \
         train_test_split(X, Y, test_size=0.2, random_state=1)

# 建立線性回歸模型並擬合訓練集數據
model = LinearRegression()
model.fit(X_train, Y_train)

# 使用測試集進行預測
Y_pred = model.predict(X_test)

# 計算模型的性能指標
r2 = r2_score(Y_test, Y_pred)
print(f"R-squared Score    :{r2:.3f}")

# 查看模型的截距和係數
intercept = model.intercept_
coefficients = model.coef_
print(f"截距 (b0)    : {intercept:.3f}")
print(f"係數 (b1, b2): {coefficients.round(3)}")

# 儲存模型
dump(model, 'boston_model.joblib')


