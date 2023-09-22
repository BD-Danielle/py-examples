# ch29_5.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 假設的郵件數據集
spam_emails = [
    "Get a free gift card now!",
    "Limited time offer: Claim your prize!",
    "You have won a free iPhone!",
]

ham_emails = [
    "Meeting rescheduled for tomorrow",
    "Can we discuss the report later?",
    "Thank you for your prompt reply",
]

# 建立資料集和對應的標籤, 1: 垃圾郵件, 0: 正常郵件
emails = spam_emails + ham_emails
labels = [1] * len(spam_emails) + [0] * len(ham_emails)

# 使用CountVectorizer來轉換郵件內容為數字矩陣
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(emails)

# 使用Multinomial Naive Bayes模型來訓練
classifier = MultinomialNB()
classifier.fit(features, labels)

# 測試分類器
print("測試分類器與結果")
test_email = ["Claim your free gift now"]
test_features = vectorizer.transform(test_email)
print(f"郵件: '{test_email[0]}' 分類結果 : \
{'垃圾郵件' if classifier.predict(test_features)[0] else '非垃圾郵件'}")

test_email = ["Can we discuss your decision tomorrow"]
test_features = vectorizer.transform(test_email)
print(f"郵件: '{test_email[0]}' 分類結果 : \
{'垃圾郵件' if classifier.predict(test_features)[0] else '非垃圾郵件'}")
