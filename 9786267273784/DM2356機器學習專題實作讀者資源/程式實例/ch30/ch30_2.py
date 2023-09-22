# ch30_2.py
from sklearn import datasets
from sklearn import tree
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import train_test_split

# 載入數據集
boston = datasets.load_boston()
X = boston.data
y = boston.target

# 分割數據集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 建立各種基本迴歸器
reg1 = tree.DecisionTreeRegressor()             # 決策樹迴歸
reg2 = KNeighborsRegressor(n_neighbors=7)       # KNN迴歸
reg3 = SVR()                                    # 支援向量機迴歸

# 建立投票迴歸器
ereg = VotingRegressor(estimators=[('dt', reg1), ('knn', reg2),
                                   ('svr', reg3)])

# 訓練投票迴歸器
ereg.fit(X_train, y_train)

# 計算訓練數據的 R 平方係數
train_score = ereg.score(X_train, y_train)
print(f"訓練數據的 R 平方係數 : {train_score}")

# 進行預測
y_pred = ereg.predict(X_test)

# 計算預測數據的 R 平方係數
test_score = ereg.score(X_test, y_test)
print(f"測試數據的 R 平方係數 : {test_score}")




