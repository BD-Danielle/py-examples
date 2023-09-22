# ch29_7.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 讀取數據
spam = pd.read_csv("spambase.csv")

# 定義特徵和目標變數
X = spam.drop(['spam'], axis=1)
y = spam['spam']

# 分割數據為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

spam_clf = MultinomialNB()

# 訓練數據
spam_clf.fit(X_train, y_train)

# 預測數據
y_pred = spam_clf.predict(X_test)

print("準確度:", accuracy_score(y_test, y_pred))




