# ch25_7.py
import pandas as pd

# 創建一個數據框
df = pd.DataFrame({
    '性別':['男', '男', '女', '男', '女', '女', '女', '男', '男', '女'],
    '喜好':['籃球', '足球', '籃球', '足球', '籃球', '足球', '籃球', '籃球',
            '棒球', '棒球']
})

# 創建交叉分析表
cross_tab = pd.crosstab(df['性別'], df['喜好'])
pd.set_option('display.unicode.east_asian_width',True)
print(cross_tab)


