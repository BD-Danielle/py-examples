# ch23_3.py
from sklearn import datasets

# 加載波士頓房價數據集
boston = datasets.load_boston()
print(f"自變數  樣本外形 : {boston.data.shape}")
print(f"目標變數樣本外形 : {boston.target.shape}")

# 輸出特徵值名稱
print("特徵值名稱")
print(boston.feature_names)

# 輸出前 3 筆自變數
print("自變數 特徵值")
print(boston.data[:3])

# 輸出前 3 筆目標變數, 房價
print("目標變數 房價")
print(boston.target[:3])

# 描述特徵值名稱
print("描述特徵值名稱")
print(boston.DESCR)



