# ch26_7.py
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

# 將類別變數轉換為數字, 使用LabelEncoder
le = LabelEncoder()
categorical_features = [i for i in data.columns if data.dtypes[i]=='object']
for col in categorical_features:
    data[col] = le.fit_transform(data[col])

# 將數據集分割為訓練集和測試集
X = data.drop('income', axis=1)
y = data['income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=5)

# 使用決策樹進行訓練
dtc = DecisionTreeClassifier(random_state=5)
dtc = dtc.fit(X_train, y_train)

# 計算與輸出特徵重要性
importances = dtc.feature_importances_
for feat, importance in zip(X.columns, importances):
    print(f'特徵 : {feat:20s} 重要性 : {importance}')

# 將特徵重要性繪製為長條圖
feature_imp = pd.Series(dtc.feature_importances_,
                        index=X.columns).sort_values(ascending=False)
feature_imp.plot(kind='bar')
plt.show()


