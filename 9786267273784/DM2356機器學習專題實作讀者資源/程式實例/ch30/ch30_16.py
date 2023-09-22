# ch30_16.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# 讀取數據
data = pd.read_csv('UCI_Credit_Card.csv')

# 定義特徵和目標變數, # 移除目標變數與ID
X = data.drop(['default.payment.next.month', 'ID'], axis=1)  
y = data['default.payment.next.month']

# 將數據分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                       test_size=0.2, random_state=10)

# 特徵縮放(標準化)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 定義基學習器和最終學習器
base_learners = [('dtc', DecisionTreeClassifier(random_state=42)), 
                 ('lr', LogisticRegression(random_state=42))]
final_estimator = SVC(random_state=10)

# 創建並訓練Stacking模型
model = StackingClassifier(estimators=base_learners, 
                           final_estimator=final_estimator)
model.fit(X_train, y_train)

# 在訓練集上進行預測並計算準確率
train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_pred)
print(f'訓練集數據準確率 Accuracy: {train_accuracy*100:.2f}%')

# 在測試集上進行預測並計算準確率
test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_pred)
print(f'測試集數據準確率 Accuracy: {test_accuracy*100:.2f}%')


