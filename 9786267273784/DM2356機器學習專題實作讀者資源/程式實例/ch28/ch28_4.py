# ch28_4.py
from joblib import load

svc = load('svc28_3.joblib')        # 載入模型
while (1):
    x = eval(input("請輸入 x 座標 : "))
    y = eval(input("請輸入 y 座標 : "))
    print(f'({x},{y}) 分類是 : {svc.predict([[x,y]])[0]}')
    z = input(f'是否繼續(y/n) : ')
    if z == 'n' or z == 'N':
        break





