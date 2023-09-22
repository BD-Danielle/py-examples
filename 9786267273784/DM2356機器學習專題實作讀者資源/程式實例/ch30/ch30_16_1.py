# ch30_16_1.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_squared_error

# 載入波士頓房價數據集
boston = datasets.load_boston()
X = boston.data
y = boston.target

# 將數據集切割成訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=42)

# 設定alpha值範圍
alphas = [0.01, 0.1, 1.0, 10.0, 100.0]

# 使用 RidgeCV 進行訓練
ridgecv = RidgeCV(alphas=alphas, cv=5)
ridgecv.fit(X_train, y_train)

# 印出最佳的 alpha
print("Best alpha:", ridgecv.alpha_)

# 對訓練集和測試集進行預測並印出R平方係數
y_train_pred = ridgecv.predict(X_train)
y_test_pred = ridgecv.predict(X_test)

print("訓練數據集 R 平方係數 : ", ridgecv.score(X_train, y_train))
print("訓練數據集 R 平方係數 : ", ridgecv.score(X_test, y_test))

# 計算和印出測試集的均方誤差
mse = mean_squared_error(y_test, y_test_pred)
print("均方誤差 :", mse)
