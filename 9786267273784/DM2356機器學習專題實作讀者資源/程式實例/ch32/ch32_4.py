# ch32_4.py
from sklearn import datasets

digits = datasets.load_digits()

# 輸出前5筆數據
print("\n前5筆數據(特徵)")
for i in range(5):
    print(f"數據 {i+1}:")
    print(digits.data[i])
    print()
print("-"*70)

# 輸出前5筆數據對應的標籤
print(f"前5筆數據對應的標籤 : {digits.target[:5]}")
print("-"*70)

# 輸出數據集描述
print(f"數據集描述 :\n{digits.DESCR}")


