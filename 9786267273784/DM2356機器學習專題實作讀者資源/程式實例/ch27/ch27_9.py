# ch27_9.py
from sklearn import datasets

# 加載鳶尾花數據集
iris = datasets.load_iris()
print(f"自變數  樣本外形 : {iris.data.shape}")
print(f"目標變數樣本外形 : {iris.target.shape}")

# 輸出特徵值名稱
print("特徵值名稱")
print(iris.feature_names)

# 描述特徵值名稱
print("描述特徵值名稱")
print(iris.DESCR)



