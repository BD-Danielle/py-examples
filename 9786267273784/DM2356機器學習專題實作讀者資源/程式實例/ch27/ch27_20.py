# ch27_20.py
import pandas as pd

# 讀取數據
df = pd.read_csv('nasa.csv')

# 刪除指定的列
df = df.drop(['Name', 'Neo Reference ID', 'Est Dia in M(min)',
              'Est Dia in M(max)', 'Est Dia in Miles(min)',
              'Est Dia in Miles(max)', 'Est Dia in Feet(min)',
              'Est Dia in Feet(max)', 'Epoch Date Close Approach',
              'Relative Velocity km per hr', 'Miles per hour',
              'Miss Dist.(Astronomical)', 'Miss Dist.(lunar)',
              'Miss Dist.(miles)', 'Equinox'],
              axis=1)


# 將 'Hazardous' 列的 True/False 轉換為 1/0
df['Hazardous'] = df['Hazardous'].map({True: 1, False: 0})

# 將 'Close Approach Date' 和 'Orbit Determination Date'
# 轉換為日期時間物件，然後再轉換為時間戳記
df['Close Approach Date'] = pd.to_datetime(df['Close Approach Date'],
                            format='%Y/%m/%d').view('int64') // 10**9
df['Orbit Determination Date'] = pd.to_datetime(df['Orbit Determination Date']).\
                                                view('int64') // 10**9

pd.set_option('display.max_columns', None)  # 顯示所有欄位
pd.set_option('display.width', 200)         # 設定顯示寬度

# 顯示前五筆數據以驗證轉換是否成功
print(df.head())










