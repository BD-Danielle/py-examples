# ch26_9.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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

# 將數據集分割為訓練集和測試集
X = data.drop('income', axis=1)
y = data['income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=5)

# 使用隨機森林進行訓練
rfc = RandomForestClassifier(n_estimators=100, random_state=5)
rfc = rfc.fit(X_train, y_train)

# 預測測試集的結果
y_pred = rfc.predict(X_test)

# 輸出預測準確度
print(f"隨機森林樹 Accuracy : {accuracy_score(y_test, y_pred):.3f}")
