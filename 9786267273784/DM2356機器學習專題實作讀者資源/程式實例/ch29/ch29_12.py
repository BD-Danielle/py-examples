# ch29_12.py
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 下載並載入20newsgroups數據集
data = fetch_20newsgroups()

# 將數據分成訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=20)

# 建立一個pipeline, 包含TfidfVectorizer和MultinomialNB
pipeline = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# 使用訓練數據訓練模型
pipeline.fit(X_train, y_train)

# 使用模型進行預測
y_pred = pipeline.predict(X_test)

# 計算並打印準確率
print(f"準確度 : {accuracy_score(y_test, y_pred)}")


