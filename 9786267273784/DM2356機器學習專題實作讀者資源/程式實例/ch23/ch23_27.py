# ch23_27.py
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 下載波士頓房價數據集
boston = datasets.load_boston()
X = boston.data
Y = boston.target
# 將數據分為訓練集和測試集（80-20的比例）
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,
                                                 random_state=1)

# 建立線性迴歸模型並擬合訓練集數據
linear_regression = LinearRegression()
linear_regression.fit(X_train, Y_train)

# 使用測試集進行預測
Y_pred = linear_regression.predict(X_test)

# 計算殘差
residuals = Y_test - Y_pred

# 繪製殘差圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.scatter(Y_pred, residuals, alpha=0.5)
plt.xlabel('預測房價')
plt.ylabel('殘差')
plt.title('波士頓房價的殘差圖')
plt.axhline(y=0, color='r', linestyle='--')
plt.show()



