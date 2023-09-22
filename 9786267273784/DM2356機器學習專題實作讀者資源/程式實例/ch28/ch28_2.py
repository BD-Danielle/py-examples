# ch28_2.py
import numpy as np
from sklearn import svm

# 建立10個點, 其中5個分類為A, 5個分類為B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3]])
y = np.array(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])

svc = svm.SVC(kernel = 'linear')        # 建立 linear的 svc
svc.fit(X, y)                           # 訓練 svc

print(f'權重係數           : {svc.coef_}')
print(f'截距(偏置)         : {svc.intercept_}')
print(f'支援向量索引       : {svc.support_}')
print(f'支援向量           : \n{svc.support_vectors_}')
print(f'每個類別支援向量數 : {svc.n_support_}')












