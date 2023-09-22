# ch24_4.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv('UCI_Credit_Card.csv')

# 定義特徵和目標變數, 主要是移除目標變數default.payment.next.month與ID
features = data.drop(['default.payment.next.month','ID'], axis=1)  
X = features
y = data['default.payment.next.month']            # 設定目標變數

# 將數據分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                          test_size=0.2, random_state=10)

# 特徵縮放
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 創建並訓練邏輯迴歸模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 獲取特徵重要性 - 對於邏輯迴歸模型，用查看模型係數來判斷特徵的重要性
importance = model.coef_[0]

# 總結特徵重要性
for i, score in enumerate(importance):
    print(f'特徵: {features.columns[i]:10s}, 分數: {score:.5f}')

# 繪製特徵重要性
plt.figure(figsize=(10, 6))                         # 設置圖表大小
plt.bar([x for x in range(len(importance))], importance)
plt.xticks([x for x in range(len(importance))],
           features.columns, rotation='vertical')   # 在X軸上加上特徵名稱
plt.title('UCI_Credit_Card Data')
plt.show()







