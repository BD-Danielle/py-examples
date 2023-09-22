# ch22_16.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

X, y = make_regression(n_features=1, noise=20, random_state=10)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(X, y)
plt.show()















