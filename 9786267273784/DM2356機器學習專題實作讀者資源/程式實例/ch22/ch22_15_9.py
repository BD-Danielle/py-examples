# ch22_15_9.py
from sklearn.preprocessing import LabelEncoder

# 假設我們有一個稱為"fruits"的類別型標籤列表
fruits = ['apple','apple','cherry','apple','cherry','orange']

# 創建一個LabelEncoder物件
label = LabelEncoder()

# 使用LabelEncoder的fit_transform()方法對fruits進行轉換
fruits_encoded = label.fit_transform(fruits)
print(fruits_encoded)

# 用inverse_transform()方法將數字標籤轉換回原來的文字標籤
print(label.inverse_transform(fruits_encoded))


