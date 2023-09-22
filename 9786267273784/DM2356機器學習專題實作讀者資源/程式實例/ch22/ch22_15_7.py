# ch22_15_7.py
import pandas as pd

# 讀取CSV文件
df = pd.read_csv('個人資料.csv')

# 列出所有的欄位名稱
print(df.columns)

# 你可以將下面的字典修改為你需要轉換的欄位名稱
# key為原本的中文名稱，value為你想轉換成的英文名稱
columns = {
    '編號': 'ID',
    '學歷': 'Education'
}

# 重新命名欄位名稱
df.rename(columns=columns, inplace=True)

# 檢查新的DataFrame, set_option()可以對齊欄位
pd.set_option('display.unicode.east_asian_width',True)
print(df.head())






