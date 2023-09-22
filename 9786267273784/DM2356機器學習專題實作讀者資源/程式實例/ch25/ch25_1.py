# ch25_1.py
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# 定義特徵和目標變數
features = [['晴', '熱', '弱'], ['晴', '熱', '強'], ['陰', '熱', '弱'], 
            ['雨', '涼', '弱'], ['雨', '冷', '弱'], ['雨', '冷', '強'],
            ['陰', '冷', '強']]
labels = ['是', '否', '是', '是', '否', '否', '是']

# 將特徵矩陣轉換為數字編碼
label_encoders = []
features_encoded = []
for i in range(len(features[0])):
    le = LabelEncoder()
    feature_encoded = le.fit_transform([row[i] for row in features])    # 建立1x7編碼
    features_encoded.append(feature_encoded)        # 將 1x7 存入 features_encoded
    label_encoders.append(le)                       # 儲存每列特徵的文字轉數字編碼規則
features_encoded = np.array(features_encoded).T     # 二維轉置, 從 3 x 7 轉成 7 x 3
print(f'特徵標籤編碼\n{features_encoded}')

# 將目標變數轉換為數字編碼
label_encoder_label = LabelEncoder()
labels_encoded = label_encoder_label.fit_transform(labels)
print(f'目標變數編碼\n{labels_encoded}')

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier()
dtc.fit(features_encoded, labels_encoded)

# 用新的觀察值來進行預測
test_features = [['晴', '涼', '弱']]
test_features_encoded = np.zeros((1, len(test_features[0]))) # 建立二維陣列,暫定元素為 0

# 應用 19 行儲存的編碼規則, 將文字轉成數字
for i in range(len(test_features[0])):
    test_features_encoded[0, i] = label_encoders[i].transform([test_features[0][i]])
print(f'測試數據編碼\n{test_features_encoded}')

# 輸出數字標籤
pred = dtc.predict(test_features_encoded)
print(f'預測結果 : {pred}')

# 應用24 ~ 25行的編碼規則, 將數字標籤反轉為文字標籤
print(f'預測結果 : {label_encoder_label.inverse_transform(pred)[0]}')
