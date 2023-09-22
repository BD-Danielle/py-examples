# ch32_6.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()

# 分割數據為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(digits.data,
                 digits.target, test_size=0.2, random_state=9)

# 創建決策樹分類器
clf = DecisionTreeClassifier(random_state=9)

# 使用訓練數據來訓練模型
clf.fit(X_train, y_train)

# 預測訓練集和測試集的結果
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

# 計算並輸出訓練集和測試集的準確度
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print('決策樹 DecisionTree 辨識')
print(f'訓練數據的準確度 : {train_accuracy:.3f}')
print(f'測試數據的準確度 : {test_accuracy:.3f}')
print("-"*70)

# 輸出預測數據的真實值與目標值
y_pred = clf.predict(X_test)
print(f"測試的真實值\n{y_test}")
print("-"*70)
print(f"預測的目標值\n{y_pred}")
print("-"*70)



