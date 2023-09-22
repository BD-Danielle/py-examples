# ch23_14.py
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# 加載波士頓房價數據集
boston = datasets.load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target          # 加上目標欄位的房價欄位

# 繪製 3D 圖表
fig = plt.figure()
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
ax = fig.add_subplot(projection='3d')
ax.scatter(df['LSTAT'],df['RM'],df['MEDV'])
ax.set_xlabel('低收入比例')
ax.set_ylabel('房間數')
ax.set_zlabel('房價')
plt.show()



