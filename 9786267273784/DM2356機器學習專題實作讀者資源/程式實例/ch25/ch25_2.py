# ch25_2.py
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 加載葡萄酒數據集
wine = load_wine()

# 分割數據集
X_train,X_test,y_train,y_test = train_test_split(
    wine.data,wine.target, test_size=0.2,random_state=9)

# 建立決策樹
dtc = DecisionTreeClassifier()

# 訓練分類器
dtc.fit(X_train, y_train)

# 進行預測
y_pred = dtc.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("="*70)   
print(f'預測第 1 個標籤                 : {y_pred[0]}')
print(f'預測第 1 個標籤屬於各分類的機率 : {dtc.predict_proba(X_test[:1])}')
print("="*70)

# 計算 accuracy
acc = accuracy_score(y_test, y_pred)
print(f"方法 1 測試數據準確率(Accuracy Score) : {acc}")

# 另一種方法輸出準確率
print(f'方法 2 訓練數據準確率 : {dtc.score(X_train, y_train)}')
print(f'方法 2 測試數據準確率 : {dtc.score(X_test, y_test)}')








