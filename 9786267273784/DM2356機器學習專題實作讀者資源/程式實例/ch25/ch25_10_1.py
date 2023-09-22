# ch25_10_1.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# 數據預處理
for column in df.columns:
    if df[column].dtype == type(object):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
# 定義特徵和目標變數
X = df.drop('Churn', axis=1)
y = df['Churn']
# 分割數據集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                          test_size=0.3, random_state=5)
# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier(max_depth=5)
dtc.fit(X_train, y_train)
# 進行預測
y_pred = dtc.predict(X_test)
# 評估模型
print(f"準確率(Accuracy Score):{accuracy_score(y_test,y_pred):.2f}")
print("-"*70)
# 計算混淆矩陣並輸出
conf_mat = confusion_matrix(y_test, y_pred)
print(f"混淆矩陣(Confusion Matrix):\n{conf_mat}")
print("-"*70)
# 輸出分類報告
print(classification_report(y_test, y_pred))


