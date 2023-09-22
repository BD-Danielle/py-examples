# ch23_21.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('data23_19.csv')
X = pd.DataFrame(df.x)

# 使用 PolynomialFeatures 生成一元二次多項式特徵
degree = 2                      
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

# 列印生成的多項式特徵
print(poly.get_feature_names_out())
print(X_poly)


