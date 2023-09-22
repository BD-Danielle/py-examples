# ch29_3.py
from sklearn.feature_extraction.text import CountVectorizer

# 創建 CountVectorizer 實例
vectorizer = CountVectorizer()

# 多行句子進行擬合和轉換
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]
X = vectorizer.fit_transform(corpus)

# 輸出得到的結果
print(vectorizer.get_feature_names_out())
print(X.toarray())
