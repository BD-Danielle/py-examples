# ch24_1.py
from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# 20個申請人，包括年齡、年收入、已有的債務金額
applicants = np.array([
    [25, 50000, 10000],
    [35, 60000, 8000],
    [45, 70000, 12000],
    [55, 80000, 10000],
    [65, 60000, 9000],
    [30, 40000, 12000],
    [40, 70000, 8000],
    [50, 60000, 10000],
    [60, 80000, 8000],
    [33, 50000, 11000],
    [26, 55000, 15000],
    [36, 65000, 7500],
    [46, 75000, 13000],
    [56, 85000, 10000],
    [66, 65000, 8500],
    [31, 45000, 11000],
    [41, 75000, 8500],
    [51, 65000, 9500],
    [61, 85000, 8500],
    [34, 55000, 12000]
])

# 對應的違約記錄, 1 表示違約, 0 表示未違約
defaults = np.array([1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1])

# 拆分資料集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(applicants,
                          defaults, test_size=0.2, random_state=10)

# 建立邏輯迴歸模型
model = LogisticRegression()

# 使用訓練集訓練模型
model.fit(X_train, y_train)

# 使用模型對測試集進行預測
y_pred = model.predict(X_test)
print(f"準確度 Accuracy : {accuracy_score(y_test, y_pred)}")
print(f"測試數據真實\n{y_test}")
print(f"測試數據預估\n{y_pred}")

dump(model, 'bank_ch24_1.joblib')   # 儲存模型

