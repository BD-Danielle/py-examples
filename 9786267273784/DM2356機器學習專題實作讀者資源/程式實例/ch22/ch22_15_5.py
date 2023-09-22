# ch35_5.py
from sklearn.metrics import confusion_matrix

# 假設已經有了實際目標變數值和模型預測的目標變數值
y_true = [1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 1, 1, 0, 1]

# 生成混淆矩陣
cm = confusion_matrix(y_true, y_pred)
print("混淆矩陣 :")
print(cm)


