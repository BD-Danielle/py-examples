# ch27_11.py
import pandas as pd
iris = pd.Series([0, 1, 2])
print(f"執行 map() 前 \n{iris}")
iris = iris.map({0:'setosa',1: 'versicolor',2: 'virginica'})
print(f"執行 map() 後 \n{iris}")


