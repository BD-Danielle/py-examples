# ch30_11.py
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LinearRegression

# 加載數據集
boston = load_boston()
X = boston.data
y = boston.target

# 將數據分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=42)

# 創建LinearRegressor模型
linear_reg = LinearRegression()

# AdaBoost迴歸模型, 使用LinearRegressor作為基本學習模型
# 設定迭代次數為50次, 學習率設 0.6
ada_reg = AdaBoostRegressor(base_estimator=linear_reg, n_estimators=50,
                            learning_rate=0.6, random_state=9)

# 使用訓練數據來訓練模型
ada_reg.fit(X_train, y_train)

# 計算訓練集的R平方係數
train_r2 = ada_reg.score(X_train, y_train)
print(f'訓練集的R平方係數 : {train_r2}')

# 計算測試集的R平方係數
test_r2 = ada_reg.score(X_test, y_test)
print(f'測試集的R平方係數 : {test_r2}')


