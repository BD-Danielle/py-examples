# ch29_15.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# 讀取CSV檔案
data = pd.read_csv('IMDB Dataset.csv')

# 使用TfidfVectorizer轉換文件
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['review'])
y = data['sentiment']

# 將數據集分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 使用多項式單純貝氏分類器
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# 在測試集上進行預測
predictions = classifier.predict(X_test)

# 輸出準確度和分類報告
print(f"準確度   : {accuracy_score(y_test, predictions)}")
print(f"分類報告 : {classification_report(y_test, predictions)}")

# 預測新的評論
new_reviews = ['This movie is fantastic! I like it because it is so good!',
               'I hate this movie. It is terrible and very boring.',
               'This movie is not good but not bad either. It is average.']
new_reviews_transformed = vectorizer.transform(new_reviews)
new_predictions = classifier.predict(new_reviews_transformed)

for sentence, prediction in zip(new_reviews, new_predictions):
    print("評論 \"{}\" 是 : {}".format(sentence, prediction))




