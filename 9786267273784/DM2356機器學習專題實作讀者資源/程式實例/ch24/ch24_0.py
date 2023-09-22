# ch24_0.py
import numpy as np

def logistic_regression(beta0, beta1, x):
    return 1 / (1 + np.exp(-(beta0 + beta1 * x)))

beta0 = -6.5
beta1 = 0.0002

x_values = [4000, 80000]

for x in x_values:
    print(f'x = {x:5d}, logistic迴歸輸出 {logistic_regression(beta0,beta1,x)}')


