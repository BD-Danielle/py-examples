# ch30_1.py
from sklearn import datasets
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 載入鳶尾花數據集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 分割數據集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 建立各種基本分類器
clf1 = tree.DecisionTreeClassifier()            # 決策樹
clf2 = KNeighborsClassifier(n_neighbors=5)      # KNN
clf3 = SVC(probability=True)                    # 支援向量機

# 建立投票分類器，這裡使用了軟投票
eclf = VotingClassifier(estimators=[('dt', clf1), ('knn', clf2),
                                    ('svc', clf3)], voting='soft')

# 訓練投票分類器
eclf.fit(X_train, y_train)

# 訓練集準確度
train_predictions = eclf.predict(X_train)
train_accuracy = accuracy_score(y_train, train_predictions)
print(f'訓練資料集準確度 : {train_accuracy}')

# 測試集準確度
test_predictions = eclf.predict(X_test)
test_accuracy = accuracy_score(y_test, test_predictions)
print(f'測試資料集準確度 : {test_accuracy}')




