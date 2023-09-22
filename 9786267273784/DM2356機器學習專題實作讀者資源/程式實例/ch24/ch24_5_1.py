# ch24_5.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv('UCI_Credit_Card.csv')

# 定義特徵和目標變數
X = data[['PAY_0', 'BILL_AMT1']]    # 只使用 'PAY_0' 和 'BILL_AMT1'
y = data['default.payment.next.month']

# 特徵縮放
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 將數據分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                          test_size=0.2, random_state=10)

# 創建並訓練邏輯迴歸模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 在訓練集上進行預測並計算準確率
train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_pred)
print(f'訓練集數據準確率 Accuracy: {train_accuracy*100:.2f}%')

# 在測試集上進行預測並計算準確率
test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_pred)
print(f'測試集數據準確率 Accuracy: {test_accuracy*100:.2f}%')

plt.figure(figsize=(10, 8))
plt.scatter(X[y==0, 0], X[y==0, 1], label='Class 0')
plt.scatter(X[y==1, 0], X[y==1, 1], label='Class 1')
plt.xlabel('PAY_0')
plt.ylabel('BILL_AMT1')
plt.legend()
plt.show()
