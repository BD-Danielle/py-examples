# ch13_1.py
base = 10000
rate = 0.03
year = 10
for i in range(1, year+1):
    base = base + base*rate
    print(f'經過 {i:2d} 年後累積金額 {base:.2f}')












