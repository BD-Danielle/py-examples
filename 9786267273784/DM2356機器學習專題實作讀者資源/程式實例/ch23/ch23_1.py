# ch23_1.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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

# 建立線性迴歸模型並擬合訓練集數據
linear_regression = LinearRegression()
linear_regression.fit(X, Y)

# 查看模型的截距和係數
intercept = linear_regression.intercept_
coefficients = linear_regression.coef_

print(f"截距 (b0)    : {intercept:.3f}")
print(f"係數 (b1, b2): {coefficients.round(3)}")
print("-"*70)

# 請輸入身高和腰圍, 然後預測體重
h = eval(input("請輸入身高 : "))
w = eval(input("請輸入腰圍 : "))
new_weight = pd.DataFrame(np.array([[h, w]]),
                          columns=["height","waist"])
predicted_weight = linear_regression.predict(new_weight)
print(f"預測體重 : {predicted_weight[0]:.2f}")


                                
