# ch22_15_4.py
from sklearn.metrics import classification_report

# 假設已經有了實際目標變數值和模型預測的目標變數值
y_true = [1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 1, 1, 0, 1]

# 生成分類報告
report = classification_report(y_true, y_pred)
print("分類報告 :")
print(report)







