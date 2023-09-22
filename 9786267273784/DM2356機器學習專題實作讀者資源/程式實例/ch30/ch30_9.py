# ch30_9.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# 讀取數據
df = pd.read_csv('diabetes_new.csv')

# 定義特徵和目標
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# 分割訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=5)

# 特徵縮放(標準化)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立AdaBoost分類器模型
model = AdaBoostClassifier(n_estimators=100, learning_rate=0.5,
                           random_state=5)
model.fit(X_train, y_train)

# 預測訓練集和測試集
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 計算並列印訓練數據和測試數據的準確度
print(f"訓練數據的準確度 : {accuracy_score(y_train, y_train_pred):.5f}")
print(f"測試數據的準確度 : {accuracy_score(y_test, y_test_pred):.5f}")


