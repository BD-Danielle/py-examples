# ch28_21.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# 讀取數據集
df = pd.read_csv('auto-mpg.csv')

# 將 '?' 替換為 NaN，並刪除含有缺失值的行
df.replace('?', np.nan, inplace=True)
df.dropna(inplace=True)

# 去除汽車型號這一列
df = df.drop(columns=['car name'])

# 將數據分割成特徵和目標
X = df.drop('mpg', axis=1)
y = df['mpg']

# 將資料型態轉換為 float
X = X.astype(float)
y = y.astype(float)

# 分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 標準化數據
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立並訓練模型
model_linear = SVR(kernel='linear')                     # linear模型
model_linear.fit(X_train, y_train)

model_rbf = SVR(kernel='rbf')                           # rbf模型
model_rbf.fit(X_train, y_train)

# 預測訓練數據
y_pred_train_linear = model_linear.predict(X_train)
y_pred_train_rbf = model_rbf.predict(X_train)

# 預測測試數據
y_pred_test_linear = model_linear.predict(X_test)
y_pred_test_rbf = model_rbf.predict(X_test)

# 計算並輸出 R平方係數
print("訓練數據R平方係數linear: ", r2_score(y_train, y_pred_train_linear))
print("測試數據R平方係數linear: ", r2_score(y_test, y_pred_test_linear))
print("-"*70)
print("訓練數據R平方係數 rbf  : ", r2_score(y_train, y_pred_train_rbf))
print("測試數據R平方係數 rbf  : ", r2_score(y_test, y_pred_test_rbf))
print("-"*70)

# 創建並列印預測值和實際值的數據框
df_pred_linear = pd.DataFrame({'  實際 MPG': y_test,\
                               '預測 MPG (Linear)': y_pred_test_linear})
df_pred_rbf = pd.DataFrame({'  實際 MPG': y_test,\
                            '預測 MPG (RBF)': y_pred_test_rbf})

print(df_pred_linear)
print(df_pred_rbf)
