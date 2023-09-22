# ch29_4.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 準備本文數據和對應的類別標籤
corpus = [
    'Gravity is the force that attracts two bodies toward each other.',
    'Shakespeare was an English playwright, poet, and actor.',
    'Literary criticism is the study, evaluation, and interpretation of literature.',
    'Quantum mechanics is a fundamental theory in physics.',
    'The theory of relativity is the greatest physical law of the 20th century.',
    'A novel is also a form of literary work.'
]
y = ['physics', 'literature', 'literature', 'physics', 'physics', 'literature']

# 創建 CountVectorizer 實例並轉換本文數據
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# 創建一個 MultinomialNB 物件並訓練模型
clf = MultinomialNB()
clf.fit(X, y)

# 預測新的句子
new_docs = ["Einstein developed the theory of relativity.", 
            "Pride and Prejudice is a novel by Jane Austen."]
new_X = vectorizer.transform(new_docs)
pred_y = clf.predict(new_X)

print(f'{new_docs[0]} : {pred_y[0]}')
print(f'{new_docs[1]} : {pred_y[1]}')

