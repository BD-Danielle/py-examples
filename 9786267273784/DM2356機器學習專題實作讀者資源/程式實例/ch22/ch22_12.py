# ch22_12.py
from joblib import load

# 載入模型
model = load('model_ch22_11.joblib')

h = eval(input("請輸入身高(公分) : "))
h /= 100
weight_pred = model.predict([[h]])  # 預測 體重 數據
print(f"預估體重是 : {weight_pred[0]:.2f} 公斤")


