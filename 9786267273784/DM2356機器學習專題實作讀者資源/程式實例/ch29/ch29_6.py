# ch29_6.py
import pandas as pd

# 讀取數據
spam = pd.read_csv("spambase.csv")
print(f'spambase數據外形 : {spam.shape}')
print(f'前 5 筆資料\n{spam.head()}')
print(spam.info())
print(f'輸出正常郵件和垃圾郵件數量')
spam['spam'] = spam['spam'].replace({0: '正常郵件', 1: '垃圾郵件'})
print(spam['spam'].value_counts())





