# ch30_15.py
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

data = fetch_california_housing()

# 分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(data.data,
                 data.target, test_size=0.2, random_state=42)

# 初始化 GradientBoostingRegressor 模型
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
                                  max_depth=3, random_state=42)

# 使用訓練集訓練模型
model.fit(X_train, y_train)

# 計算訓練集的 R 平方係數
train_score = model.score(X_train, y_train)
print(f"訓練數據的 R 平方係數 : {train_score}")

# 計算測試集的 R 平方值
test_score = model.score(X_test, y_test)
print(f"測試數據的 R 平方係數 : {test_score}")



