# ch27_8.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 讀取csv文件
data = pd.read_csv('adult.csv')

# 數據清洗, 將'?'替換為 np.nan
data = data.replace('?', np.nan)

# 刪除包含缺失值的列
data = data.dropna()

# 將類別變量轉換為數字, 使用LabelEncoder
le = LabelEncoder()
categorical_features = [i for i in data.columns if data.dtypes[i]=='object']
for col in categorical_features:
    data[col] = le.fit_transform(data[col])

# 使用所有特徵訓練決策樹模型並計算特徵重要性
X = data.drop('income', axis=1)
y = data['income']
dtc = DecisionTreeClassifier()
dtc = dtc.fit(X, y)
importances = dtc.feature_importances_
features = X.columns

# 獲得最重要的7個特徵
indices = np.argsort(importances)[-7:]
top_features = [features[i] for i in indices]

# 使用最重要的7個特徵分割數據集並訓練模型
X = data[top_features]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=5)

dtc = DecisionTreeClassifier(random_state=5)
dtc = dtc.fit(X_train, y_train)

# 預測測試集的結果
y_pred = dtc.predict(X_test)

# 輸出預測準確度
print(f"7個特徵決策樹 Accuracy : {accuracy_score(y_test, y_pred):.3f}")


