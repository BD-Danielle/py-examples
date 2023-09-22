# ch28_9.py
from sklearn.datasets import make_circles
from sklearn import svm
import numpy as np

# 生成數據
X, y = make_circles(n_samples=200, noise=0.05, random_state=10)
z = X[:,0]**2 + X[:,1]**2               # 增加 z 軸數據

features = np.concatenate((X, z.reshape(-1,1)), axis=1)
svc = svm.SVC(kernel = 'linear')
svc.fit(features, y)

print(f'權重係數           : {svc.coef_}')
print(f'截距(偏置)         : {svc.intercept_}')


