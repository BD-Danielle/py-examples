# ch29_19.py
import jieba
from sklearn.feature_extraction.text import CountVectorizer

# 將句子切分成詞語
text = ["我最喜歡的學校是台塑企業集團的明志工專",
        "台塑企業創辦明志工專",
        "現在稱明志科技大學"]
text = [" ".join(jieba.cut(sentence)) for sentence in text]

# 使用CountVectorizer處理
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

# 輸出結果
print(vectorizer.get_feature_names_out())
print(X.toarray())
