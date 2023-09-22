# ch22_17.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X, y = make_regression(n_features=1, noise=20, random_state=10)

# 數據分割為X_train,y_train訓練數據, X_test,y_test測試數據
X_train, X_test, y_train, y_test = \
         train_test_split(X, y, test_size=0.2, random_state=10)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  
plt.rcParams["axes.unicode_minus"] = False  # 可以顯示負號
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(X_train,y_train,label="訓練數據")
plt.scatter(X_test,y_test,label="測試數據")
plt.legend()
plt.show()















