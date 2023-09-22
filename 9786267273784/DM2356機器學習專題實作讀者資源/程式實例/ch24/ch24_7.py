# ch24_7.py
from sklearn import datasets

# 加載葡萄酒數據集
wine = datasets.load_wine()
print(f"自變數  樣本外形 : {wine.data.shape}")
print(f"目標變數樣本外形 : {wine.target.shape}")

# 輸出特徵值名稱
print("自變數特徵值名稱")
print(wine.feature_names)

# 輸出前 3 筆自變數
print("自變數 特徵值")
print(wine.data[:3])

# 輸出前 3 筆目標變數, 
print("目標變數 品種")
print(wine.target[:3])

# 描述特徵值名稱
print("描述特徵值名稱")
print(wine.DESCR)



