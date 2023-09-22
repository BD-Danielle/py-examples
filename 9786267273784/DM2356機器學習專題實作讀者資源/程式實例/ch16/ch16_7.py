# ch16_7.py
import pandas as pd
import numpy as np

# 假設我們有一個包含每日日期的數據集
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
df = pd.DataFrame(data={'date': dates})

# 我們可以從日期中提取出 'day of year' 這個特徵
df['day_of_year'] = df['date'].dt.dayofyear

# 然後我們可以用正弦和餘弦函數來表示這個特徵的週期性
# 我們假設一年有365天，將 'day of year' 轉換為 2 * pi 的範圍
df['sin_day_of_year'] = np.sin(2 * np.pi * df['day_of_year'] / 365)
df['cos_day_of_year'] = np.cos(2 * np.pi * df['day_of_year'] / 365)

# 現在我們就有了兩個可以表示 'day of year' 週期性的特徵
print(df.head())


