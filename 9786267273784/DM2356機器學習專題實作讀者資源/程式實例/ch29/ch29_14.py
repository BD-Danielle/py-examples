# ch29_14.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 數據集有10個電影評論，以及對應的標籤
reviews = ['I love this movie', 'I hate this movie',
           'I enjoyed this movie', 'This is a terrible movie', 
           'Absolutely fantastic', 'What a waste of time',
           'Two thumbs up', 'Avoid at all costs', 
           'This film was delightful', 'Not my cup of tea']
labels = ['positive', 'negative', 'positive', 'negative', 'positive',
          'negative', 'positive', 'negative', 'positive', 'negative']

# 將文本數據轉換為數字表示
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# 使用單純貝氏分類器訓練模型
classifier = MultinomialNB()
classifier.fit(X, labels)

# 使用模型預測新的句子的情緒
new_sentences = ["I really enjoyed the plot and the characters",
                 "waste my costs"]
new_vectors = vectorizer.transform(new_sentences)
new_predictions = classifier.predict(new_vectors)

for sentence, prediction in zip(new_sentences, new_predictions):
    print("評論 \"{}\" 是 : {}".format(sentence, prediction))


