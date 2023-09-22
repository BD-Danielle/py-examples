# ch22_15_1.py
from sklearn.metrics import accuracy_score

y_true = [1, 1, 2, 2, 3, 3]     # 真實的標籤
y_pred = [1, 1, 2, 2, 3, 2]     # 模型預測的標籤
# 輸出準確度
print(f"Accuracy Score : {accuracy_score(y_true, y_pred)}")  
