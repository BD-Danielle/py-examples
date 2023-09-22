# ch29_16.py
from sklearn.feature_extraction.text import CountVectorizer

# 創建 CountVectorizer 實例物件
vectorizer = CountVectorizer()

# 句子進行擬合和轉換
corpus = [
    '明志科技大學是台灣頂尖的科技大學',
]
X = vectorizer.fit_transform(corpus)

# 輸出得到的結果
print(f'詞彙表 : {vectorizer.get_feature_names_out()}')
print(f'陣列 : {X.toarray()}')


