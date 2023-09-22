# ch30_17.py
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.ensemble import StackingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import RidgeCV
from sklearn.svm import SVR

# 加載數據集
boston = load_boston()
X = boston.data
y = boston.target

# 將數據分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=42)

# 建立基學習器
base_learners = [
                 ('svr', SVR()),
                 ('dtr', DecisionTreeRegressor(random_state=10))
                ]

# 建立元學習器
meta_learner = RidgeCV()

# 建立堆疊迴歸器
stack_reg = StackingRegressor(estimators=base_learners,
                              final_estimator=meta_learner)

# 使用訓練數據來訓練模型
stack_reg.fit(X_train, y_train)

# 計算訓練集的R平方係數
train_r2 = stack_reg.score(X_train, y_train)
print(f'訓練集的R平方係數 : {train_r2}')

# 計算測試集的R平方係數
test_r2 = stack_reg.score(X_test, y_test)
print(f'測試集的R平方係數 : {test_r2}')


