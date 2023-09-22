# ch29_2.py
from sklearn.feature_extraction.text import CountVectorizer

# 創建 CountVectorizer 實例物件
vectorizer = CountVectorizer()

# 句子進行擬合和轉換
corpus = [
    'This document is the second document.',
]
X = vectorizer.fit_transform(corpus)

# 輸出得到的結果
print(f'詞彙表 : {vectorizer.get_feature_names_out()}')
print(f'X 資料類型 : {type(X)}')
print(f'稀疏矩陣\n{X}')
print(f'陣列 : {X.toarray()}')


