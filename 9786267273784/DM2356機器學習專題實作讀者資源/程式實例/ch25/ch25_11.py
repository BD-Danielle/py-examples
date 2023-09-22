# ch25_11.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 將類別型特徵轉換為數字
label_encoders = {}
for column in df.columns:
    if df[column].dtype == type(object):
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])

# 分割特徵和標籤
X = df.drop('Churn', axis=1)
y = df['Churn']

# 切割訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=5)

# 建立並訓練決策樹模型
dtc = DecisionTreeClassifier(max_depth=5)
dtc.fit(X_train, y_train)

# 輸出每個特徵的重要性
importances = dtc.feature_importances_
for feat, importance in zip(X.columns, importances):
    print(f'特徵 : {feat:20s} 重要性 : {importance}')

# 將特徵重要性繪製為長條圖
feature_imp = pd.Series(dtc.feature_importances_,
                        index=X.columns).sort_values(ascending=False)
feature_imp.plot(kind='bar')
plt.show()



