# ch22_15_2.py
from sklearn.metrics import recall_score

y_true = [1, 1, 0, 0, 1, 1]     # 真實的標籤
y_pred = [1, 0, 0, 0, 1, 1]     # 模型預測的標籤
# 輸出召回率
print("Recall Score: ", recall_score(y_true, y_pred))  


