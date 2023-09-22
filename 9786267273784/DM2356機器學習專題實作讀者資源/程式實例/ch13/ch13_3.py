# ch13_3.py
base = 100
rate = 0.1
year = 3
for i in range(1, year+1):
    base = base - base*rate
    print(f'經過 {i} 年後車輛殘值 {base}')












