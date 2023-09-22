# ch24_14.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score

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

# 建立邏輯迴歸模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 預測測試集
y_pred = model.predict(X_test)
print(f"測試的真實分類\n{y_test.to_numpy()}")      # 將Series物件轉成陣列
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("="*70)

# 計算並列印評估指標
print(f"Accuracy: {accuracy_score(y_test, y_pred):.5f}")
print("="*70)

print("混淆矩陣Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("="*70)

# 預測測試集樣本為正類的機率
y_scores = model.predict_proba(X_test)[:,1]
print(f"AUC-ROC: {roc_auc_score(y_test, y_scores):.5f}")


