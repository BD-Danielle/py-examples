# ch22_15_10.py
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# 定義特徵
features = [['晴', '熱', '弱'],
            ['晴', '熱', '強'],
            ['陰', '熱', '弱'], 
            ['雨', '涼', '弱'],
            ['雨', '冷', '弱'],
            ['雨', '冷', '強'],
            ['陰', '冷', '強']]

# 將特徵矩陣轉換為數字編碼
features_encoded = []
for i in range(len(features[0])):
    le = LabelEncoder()
    feature_encoded = le.fit_transform([row[i] for row in features]) # 建立1x7編碼
    features_encoded.append(feature_encoded)        # 將 1x7 存入 features_encoded
features_encoded = np.array(features_encoded).T     # 二維轉置, 從 3x7 轉成 7x3
print(f'特徵標籤編碼\n{features_encoded}')

