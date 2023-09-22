# ch22_18.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

X, y = make_regression(n_features=1, noise=20, random_state=10)

# 數據分割為X_train,y_train訓練數據, X_test,y_test測試數據
X_train, X_test, y_train, y_test = \
         train_test_split(X, y, test_size=0.2, random_state=10)

model = linear_model.LinearRegression()       # 建立線性模組物件
model.fit(X_train, y_train)
print(f'斜率  = {model.coef_[0]:.2f}')
print(f'截距  = {model.intercept_:.2f}')

y_pred = model.predict(X_test)
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    
plt.rcParams["axes.unicode_minus"] = False              
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(X_train,y_train,label="訓練數據")
plt.scatter(X_test,y_test,label="測試數據")
# 使用測試數據 X_test 和此 X_test 預測的 y_pred 繪製迴歸直線
plt.plot(X_test, y_pred, color="red")

# 將測試的 y 與預測的 y_pred 計算決定係數
r2 = r2_score(y_test, y_pred)                           
print(f'R平方係數 = {r2:.2f}')

plt.legend()
plt.show()















