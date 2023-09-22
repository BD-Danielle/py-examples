# ch23_18.py
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

# 繪製 3D 圖表 -- 散點圖是真實房價
fig = plt.figure()
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號
ax = fig.add_subplot(projection='3d')
ax.scatter(df['LSTAT'],df['RM'],Y)

# 繪製 3D 圖表 -- 平面是預估房價
x = np.arange(0, 40, 1)     # 低收入比例
y = np.arange(0, 10, 1)     # 房間數
x_surf, y_surf = np.meshgrid(x, y)
z = lambda x, y: (model.intercept_ + model.coef_[0] * x + model.coef_[1] * y)
ax.plot_surface(x_surf, y_surf, z(x_surf, y_surf), color='None', alpha=0.2)
ax.set_xlabel('低收入比例')
ax.set_ylabel('房間數')
ax.set_zlabel('房價')
ax.set_title('Boston真實房價 與 預估房價') 
plt.show()



