# ch25_14.py
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

# 假設我們有一些房地產數據, X代表房子面積, y代表房價
X = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])     
y = np.array([150000, 180000, 200000, 230000, 260000, 280000,
              300000, 330000, 360000, 380000, 400000])               

X = X.reshape(-1, 1)    # 改變形狀以符合sklearn的要求

# 分割數據為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=5)

# 建立決策樹迴歸模型
tree_reg = DecisionTreeRegressor(max_depth=3, random_state=10)

# 擬合模型
tree_reg.fit(X_train, y_train)

# 進行預測
y_pred = tree_reg.predict(X_test)

# R平方係數
r2 = r2_score(y_test, y_pred)

# 輸出預測結果
print(f'R平方係數 : {r2}')
print(f'實際房價 : {y_test}')
print(f'預測房價 : {y_pred}')
