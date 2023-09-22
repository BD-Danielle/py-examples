# ch25_3.py
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# 加載葡萄酒數據集
wine = load_wine()
X = wine.data[:,:2]         # 使用前 2 個特徵

# 分割數據集
X_train,X_test,y_train,y_test = train_test_split(
    X, wine.target, test_size=0.2,random_state=9)

# 建立 max_depth=1 決策樹
dtc1 = DecisionTreeClassifier(max_depth=1)
dtc1.fit(X_train, y_train)
y_pred = dtc1.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("-"*70)
acc = accuracy_score(y_test, y_pred)
print(f"max_depth=1 準確率(Accuracy Score) : {acc:.2f}")
print("="*70)

# 建立 max_depth=3 決策樹
dtc3 = DecisionTreeClassifier(max_depth=3)
dtc3.fit(X_train, y_train)
y_pred = dtc3.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("-"*70)
acc = accuracy_score(y_test, y_pred)
print(f"max_depth=3 準確率(Accuracy Score) : {acc:.2f}")

# 儲存 max_depth=3 決策樹模型
dump(dtc3, 'dtc3.joblib')





