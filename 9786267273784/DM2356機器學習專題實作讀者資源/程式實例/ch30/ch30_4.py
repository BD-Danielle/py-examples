# ch30_4.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('mushrooms.csv')
# 將特徵 'class' 分開, 這是我們的目標變數
X = df.drop('class', axis=1)
y = df['class']

# 使用 LabelEncoder, 將所有的分類特徵轉換為數值形式
le = LabelEncoder()
for column in X.columns:
    X[column] = le.fit_transform(X[column])

# 將目標變數轉換為數值形式
y = le.fit_transform(y)

# 將數據集分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=1)

# 初始化一個裝袋分類器, 預設是決策樹
bagging_clf = BaggingClassifier(n_estimators=100, random_state=1)

# 在訓練集上訓練模型, 和訓練集預測
bagging_clf.fit(X_train, y_train)                   # 訓練
y_train_pred = bagging_clf.predict(X_train)         # 預測

# 計算訓練集的準確度
train_accuracy = accuracy_score(y_train, y_train_pred)
print(f'訓練集使用 Bagging 分類的準確度 : {train_accuracy:.2f}')

# 在測試集上進行預測
y_test_pred = bagging_clf.predict(X_test)

# 計算測試集的準確度
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f'測試集使用 Bagging 分類的準確度 : {test_accuracy:.2f}')



