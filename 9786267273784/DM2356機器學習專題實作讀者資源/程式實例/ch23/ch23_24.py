# ch23_24.py
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

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

# 使用測試集進行預測
X_test_poly = poly.fit_transform(X_test)
Y_pred = model.predict(X_test_poly)
print(f"測試的真實房價\n{Y_test}")
print("-"*70)
print(f"預測的目標房價\n{Y_pred.round(1)}")

# 繪製圖表
plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
plt.scatter(Y_test,Y_pred)
plt.xlabel('實際房價')
plt.ylabel('預估房價')
plt.title('實際房價 vs 預估房價') 
plt.show()


