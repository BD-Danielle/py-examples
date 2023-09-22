# ch23_17.py
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
X = pd.DataFrame(np.c_[df['LSTAT'],df['RM']], columns=['LSTAT','RM'])
Y = boston.target

# 將數據分為訓練集和測試集（這裡使用80-20的比例）
X_train, X_test, Y_train, Y_test = \
         train_test_split(X, Y, test_size=0.2, random_state=1)

# 建立線性回歸模型並擬合訓練集數據
model = LinearRegression()
model.fit(X_train, Y_train)

# 使用測試集進行預測
Y_pred = model.predict(X_test)
print(f"測試的真實房價\n{Y_test}")
print("-"*70)
print(f"預測的目標房價\n{Y_pred.round(1)}")

# 繪製圖表
plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
plt.scatter(Y_test,Y_pred)
plt.xlabel('實際房價')
plt.ylabel('預估房價')
plt.title('實際房價 vs 預估房價') 
plt.show()

