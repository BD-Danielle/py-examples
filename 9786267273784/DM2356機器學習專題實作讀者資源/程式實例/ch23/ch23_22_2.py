# ch23_22_2.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data23_19.csv')
X = pd.DataFrame(df.x)
y = df.y

# 使用 PolynomialFeatures 生成一元五次多項式特徵
degree = 5                      
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

# 建立一元五次多項式的迴歸模型
model = LinearRegression()
model.fit(X_poly, y)
y_poly_pred = model.predict(X_poly)     # 預估值供圖表使用

# 輸出 R 平方係數
print(f"R2_score = {model.score(X_poly, y):.2f}")

# 查看模型的截距和係數
intercept = model.intercept_
coeff = model.coef_
print(f"截距 (b0)                     : {intercept:.3f}")
print(f"係數 (b0, b1, b2, b3, b4, b5) : {coeff.round(3)}")

# 繪圖表
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# 在第一個子圖繪製散點圖和點的連線 
ax[0].plot(X, y_poly_pred, color='g')  # 繪製一元五次迴歸線
ax[0].scatter(df.x, df.y)
ax[0].set_title("一元五次迴歸模型 - 點的連線")

# 在第二個子圖繪製散點圖和曲線 
xx = np.linspace(1, 6 , 100)     
y_curf = lambda x: (intercept + coeff[1] * x + coeff[2] * x * x + \
                    coeff[3] * x ** 3 + \
                    coeff[4] * x ** 4 + \
                    coeff[5] * x ** 5)
ax[1].plot(xx, y_curf(xx))
ax[1].scatter(df.x, df.y)
ax[1].set_title("一元五次迴歸模型 - 曲線")

plt.show()

