# ch23_2.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 建立10筆數據的範例
data = {
    'height': [162, 160, 167, 180, 177, 168, 189, 182, 176, 169],
    'waist':  [ 71,  81,  70,  90,  95,  80,  78, 100,  84,  80],    
    'weight': [ 53,  62,  58,  71,  72,  69,  80,  91,  78,  70],
}

# 建立DataFrame
df = pd.DataFrame(data)

# 定義自變數 和 因變數(目標變數)
X = df[['height', 'waist']]
Y = df['weight']

# 將數據分為訓練集和測試集（這裡使用80-20的比例）
X_train,X_test,Y_train,Y_test = \
            train_test_split(X,Y,test_size=0.2,random_state=1)

# 建立線性迴歸模型並擬合訓練集數據
linear_regression = LinearRegression()
linear_regression.fit(X_train, Y_train)

# 使用測試集進行預測
Y_pred = linear_regression.predict(X_test)

# 計算模型的性能指標
r2 = r2_score(Y_test, Y_pred)
print(f"R-squared Score    :{r2:.2f}")

# 查看模型的截距和係數
intercept = linear_regression.intercept_
coefficients = linear_regression.coef_
print(f"截距 (b0)    : {intercept:.3f}")
print(f"係數 (b1, b2): {coefficients.round(3)}")



