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

# 建立 max_depth=5 決策樹
dtc5 = DecisionTreeClassifier(max_depth=5)
dtc5.fit(X_train, y_train)
y_pred = dtc5.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("-"*70)
acc = accuracy_score(y_test, y_pred)
print(f"max_depth=1 準確率(Accuracy Score) : {acc:.2f}")
print("="*70)

# 建立 max_depth=7 決策樹
dtc7 = DecisionTreeClassifier(max_depth=7)
dtc7.fit(X_train, y_train)
y_pred = dtc7.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("-"*70)
acc = accuracy_score(y_test, y_pred)
print(f"max_depth=7 準確率(Accuracy Score) : {acc:.2f}")







