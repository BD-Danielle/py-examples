# ch24_2.py
from joblib import load

model = load('bank_ch24_1.joblib')
age = eval(input("請輸入年齡 : "))
income = eval(input("請輸入年收入 : "))
debt = eval(input("請輸入債務 : "))

y_pred = model.predict([[age, income, debt]])
if y_pred[0] == 1:
    print("違約")
else:
    print("未違約")




