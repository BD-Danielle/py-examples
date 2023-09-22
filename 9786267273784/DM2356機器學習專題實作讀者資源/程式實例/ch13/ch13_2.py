# ch13_2.py
base = 100
rate = 1
hour = 10
for i in range(1, hour+1):
    base = base + base*rate
    print(f'經過 {i:2d} 小時後累積病毒量 {base}')












