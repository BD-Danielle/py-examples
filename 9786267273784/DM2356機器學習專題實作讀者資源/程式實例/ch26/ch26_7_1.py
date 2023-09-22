# ch26_7_1.py
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

# 將類別變量轉換為數字，使用LabelEncoder
le = LabelEncoder()
categorical_features = [i for i in data.columns if data.dtypes[i]=='object']
for col in categorical_features:
    data[col] = le.fit_transform(data[col])

# 將數據集分割為訓練集和測試集
X = data.drop('income', axis=1)
y = data['income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 使用決策樹進行訓練
dtc = DecisionTreeClassifier()
dtc = dtc.fit(X_train, y_train)

# 計算特徵重要性並繪圖
importances = dtc.feature_importances_
features = X.columns
indices = np.argsort(importances)

plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
