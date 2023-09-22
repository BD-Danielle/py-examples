# ch30_7.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# 載入數據
df = pd.read_csv('insurance.csv')

# 將數據中有非數字資料，我們需要把它們轉換成數值資料
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

# 分割特徵為目標變數
X = df.drop(columns='expenses')
y = df['expenses']

# 切分數據為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                            test_size=0.2, random_state=42)

# 創建模型實例
bagging = BaggingRegressor(n_estimators=10, random_state=42)

# 訓練模型
bagging.fit(X_train, y_train)

# 使用訓練數據進行預測，並計算 R 平方係數
y_train_pred = bagging.predict(X_train)
r2_train = r2_score(y_train, y_train_pred)

# 使用測試數據進行預測，並計算 R 平方係數
y_test_pred = bagging.predict(X_test)
r2_test = r2_score(y_test, y_test_pred)

# 顯示結果
print(f'訓練數據 R 平方係數 : {r2_train}')
print(f'測試數據 R 平方係數 : {r2_test}')
 

