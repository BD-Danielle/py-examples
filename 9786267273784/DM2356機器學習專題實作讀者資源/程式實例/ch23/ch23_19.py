# ch23_19.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data23_19.csv')

X = pd.DataFrame(df.x)
y = df.y

# 建立線性 model 
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print(f"R2_score = {model.score(X, y):.3f}")

plt.plot(X, y_pred, color='g')      # 繪製迴歸直線
plt.scatter(df.x, df.y)             # 繪製散點圖
plt.show()


