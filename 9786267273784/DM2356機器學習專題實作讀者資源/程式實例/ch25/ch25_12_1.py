# ch25_12_1.py
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 選擇特徵
selected_features = ['Contract', 'OnlineSecurity', 'tenure', 'InternetService', 'MonthlyCharges']
target = 'Churn'

# 對類別特徵進行編碼
label_encoders = {}
for column in selected_features:
    if df[column].dtype == 'object':
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])

# 對目標變數進行編碼
label_encoder_target = LabelEncoder()
df[target] = label_encoder_target.fit_transform(df[target])

# 分割數據集
X_train, X_test, y_train, y_test = train_test_split(df[selected_features], df[target], test_size=0.2, random_state=1)

# 設定要調整的參數
params = {'max_depth': [3, 5, 7, 10, 15, 20]}

# 建立決策樹模型
clf = GridSearchCV(DecisionTreeClassifier(), params, cv=5)
clf.fit(X_train, y_train)

# 顯示最佳參數
print(f'Best parameters: {clf.best_params_}')

# 進行預測
y_pred = clf.predict(X_test)

# 模型評估
print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
