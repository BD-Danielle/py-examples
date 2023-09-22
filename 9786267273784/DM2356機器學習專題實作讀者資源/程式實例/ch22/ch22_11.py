# ch22_11.py
from joblib import dump
from sklearn.linear_model import LinearRegression
import numpy as np

height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

model = LinearRegression()          # 建立線性迴歸的模型
model.fit(X=height, y=weight)       # 數據擬合模型

# 儲存模型
dump(model, 'model_ch22_11.joblib')





