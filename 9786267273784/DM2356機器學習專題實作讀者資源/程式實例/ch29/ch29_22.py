# ch29_22.py
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# 讀取檔案
fn = 'toutiao_cat_data.txt'
news = []                                       # 新聞內容
label = []                                      # 新聞分類
with open(fn, 'r', encoding='utf-8') as file:    
    for line in file:                           # 相當於逐 row 讀取
        headline_news = line.split('_!_')       # 拆分新聞欄位
        words = ' '.join(jieba.cut(headline_news[3]))
        news.append(words)                      # 加入 news
        label.append(headline_news[2])          # 加入 label

# 將數據集分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(news, label,
                                   test_size=0.2, random_state=42)

# 使用CountVectorizer處理
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# 使用多項式單純貝氏分類器
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# 在測試集上進行預測
predictions = classifier.predict(X_test)

# 輸出準確度和分類報告
print(f"準確度   : {accuracy_score(y_test, predictions)}")
print("分類報告 :")
print(classification_report(y_test, predictions, zero_division=1))

# 預測新的評論
new_news = ['林书豪加入中国职业篮球北京首钢队!',
            '清华大学荣登亚洲最佳大学']
new_news = [" ".join(jieba.cut(sentence)) for sentence in new_news]
new_news_transformed = vectorizer.transform(new_news)
new_predictions = classifier.predict(new_news_transformed)

for sentence, prediction in zip(new_news, new_predictions):
    print(f"評論 \"{sentence}\" 是 : {prediction}")




