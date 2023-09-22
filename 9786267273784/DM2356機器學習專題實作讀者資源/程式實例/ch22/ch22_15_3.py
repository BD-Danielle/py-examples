# ch22_15_3.py
from sklearn.metrics import f1_score

y_true = [1, 1, 0, 0, 1, 1]         # 真實的標籤
y_pred = [1, 0, 0, 0, 1, 1]         # 模型預測的標籤
# 輸出F1分數
print("F1 Score: ", f1_score(y_true, y_pred))  



