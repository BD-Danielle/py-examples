# ch30_13.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score

# 讀取數據
data = pd.read_csv('glass.csv')
X = data.drop('Type', axis=1)       # 'Type' 是目標變數
y = data['Type']

# 劃分訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=42)

# 建立並訓練模型
gb = GradientBoostingClassifier(random_state=42)
gb.fit(X_train, y_train)

# 進行預測
train_predictions = gb.predict(X_train)
test_predictions = gb.predict(X_test)

# 計算並輸出訓練與測試數據準確度
train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)
print(f"訓練數據準確度 : {train_accuracy}")
print(f"測試數據準確度 : {test_accuracy}")
print('-'*70)

# 印出分類報告
print("測試數據分類報表 :\n")
print(classification_report(y_test, test_predictions))


