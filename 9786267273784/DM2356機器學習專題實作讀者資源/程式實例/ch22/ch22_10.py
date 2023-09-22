# ch22_10.py
import pickle

# 載入模型
with open('model_ch22_9.pkl', 'rb') as f:
    model = pickle.load(f)

h = eval(input("請輸入身高(公分) : "))
h /= 100
weight_pred = model.predict([[h]])  # 預測 體重 數據
print(f"預估體重是 : {weight_pred[0]:.2f} 公斤")


