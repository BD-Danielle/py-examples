# ch23_4.py
from sklearn import datasets

# 加載波士頓房價數據集
boston = datasets.load_boston()

# 輸出自變數
print("自變數 特徵值")
print(boston.data)

# 輸出目標變數, 房價
print("目標變數 房價")
print(boston.target)


