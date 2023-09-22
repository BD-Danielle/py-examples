# ch22_15_5_1.py
from sklearn.metrics import roc_auc_score

# 這是真實的標籤
y_true = [0, 0, 1, 1]

# 這是分類器預測為正類的機率
y_scores = [0.1, 0.4, 0.35, 0.8]

# 使用 roc_auc_score() 函數來計算 ROC AUC 分數
auc_score = roc_auc_score(y_true, y_scores)
print(f"ROC AUC 分數: {auc_score}")




