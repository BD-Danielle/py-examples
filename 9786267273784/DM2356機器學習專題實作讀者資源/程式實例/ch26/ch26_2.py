# ch26_2.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_boston
import numpy as np

# 載入波士頓房價數據集
boston = load_boston()

# 分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(boston.data,
                 boston.target, test_size=0.2, random_state=1)

# 建立隨機森林迴歸模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# 訓練模型
rf.fit(X_train, y_train)

# 進行預測
y_pred = rf.predict(X_test)

# 計算評估指標
r2 = r2_score(y_test, y_pred)
print(f'R-squared          : {r2:.3f}')
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error : {mse:.3f}')


