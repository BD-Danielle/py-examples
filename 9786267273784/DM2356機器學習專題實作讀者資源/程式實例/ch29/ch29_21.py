# ch29_21.py
fn = 'toutiao_cat_data.txt'                     # 檔案名稱
with open(fn, 'r', encoding='utf-8') as file:    
    for line in file:                           # 相當於逐 row 讀取
        headline_news = line.split('_!_')       # 拆分新聞欄位
        break
print(headline_news)
print("-"*70)
for news in headline_news:
    print(news)



