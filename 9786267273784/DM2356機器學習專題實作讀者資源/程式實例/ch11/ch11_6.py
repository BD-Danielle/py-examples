# ch11_6.py
import numpy as np

# 假設的郵件數據集
# 定義垃圾郵件
spam_emails = [
    "Get a free gift card now!",
    "Limited time offer: Claim your prize!",
    "You have won a free iPhone!",
]
# 定義非垃圾郵件
ham_emails = [
    "Meeting rescheduled for tomorrow",
    "Can we discuss the report later?",
    "Thank you for your prompt reply",
]

# 計算單詞出現次數的函數
def count_words(emails):
    word_count = {}                     # 初始化一個字典來儲存每個單詞的計數
    for email in emails:                # 遍歷每一封郵件
        for word in email.split():      # 遍歷郵件中的每個單詞
            word = word.lower()         # 將單詞轉換為小寫
            if word not in word_count:  # 如果該單詞還未在字典中出現過
                word_count[word] = 1    # 則新增進字典並將計數設為1
            else:                       # 如果該單詞已經在字典中出現過
                word_count[word] += 1   # 則將該單詞的計數增加1
    return word_count                   # 返回單詞計數的字典

# 使用單純貝氏分類器進行垃圾郵件過濾的函數
def classify_email(email):
    words = email.lower().split()       # 將郵件內容轉換為小寫並分割成單詞
    spam_prob = np.log(prior_spam)      # 初始化垃圾郵件的機率為垃圾郵件的先驗機率
    ham_prob = np.log(prior_ham)        # 初始化正常郵件的機率為正常郵件的先驗機率
# 遍歷郵件中的每個單詞
# 如果單詞在垃圾郵件或正常郵件中出現過,
# 則將該單詞在垃圾郵件或正常郵件中出現的機率, 加到垃圾郵件或正常郵件的總機率中
# 如果單詞在垃圾郵件或正常郵件中沒有出現過,
# 則將拉普拉斯平滑因子加到垃圾郵件或正常郵件的總機率中    
    for word in words:    
        spam_prob += np.log(spam_word_prob.get(word, 1 / (total_spam_words + 2)))
        ham_prob += np.log(ham_word_prob.get(word, 1 / (total_ham_words + 2)))
# 如果垃圾郵件的總機率大於正常郵件的總機率, 則該郵件被分類為垃圾郵件
# 否則被分類為正常郵件
    return "垃圾郵件" if spam_prob > ham_prob else "非垃圾郵件"

# 計算在垃圾郵件和正常郵件中每個單詞出現的機率的函數
def word_probability(word_count, total_count):
    # 使用拉普拉斯平滑
    return {word:(count+1)/(total_count+2) for word, count in word_count.items()}  

# 計算垃圾郵件和正常郵件的先驗機率
prior_spam = len(spam_emails) / (len(spam_emails) + len(ham_emails))
prior_ham = len(ham_emails) / (len(spam_emails) + len(ham_emails))
print(f"垃圾郵件的先驗機率 : {prior_spam}")
print(f"正常郵件的先驗機率 : {prior_ham}")
print("="*70)

# 用字典對垃圾郵件和正常郵件分別進行單詞統計
spam_word_count = count_words(spam_emails)
ham_word_count = count_words(ham_emails)
print("垃圾郵件字典單詞統計")
print(spam_word_count)
print("正常郵件字典單詞統計")
print(ham_word_count)
print("="*70)

# 計算總單詞數
total_spam_words = sum(spam_word_count.values())
total_ham_words = sum(ham_word_count.values())
print(f"垃圾郵件的總單詞數 : {total_spam_words}")
print(f"正常郵件的總單詞數 : {total_ham_words}")
print("="*70)

# 對垃圾郵件和正常郵件分別進行單詞機率的計算
spam_word_prob = word_probability(spam_word_count, total_spam_words)
ham_word_prob = word_probability(ham_word_count, total_ham_words)
print("垃圾郵件字典單詞機率")
print(spam_word_prob)
print("正常郵件字典單詞機率")
print(ham_word_prob)
print("="*70)

# 測試分類器
print("測試分類器與結果")
test_email = "Claim your free gift now"
print(f"郵件: '{test_email}' 分類結果 : {classify_email(test_email)}")
test_email = "Can we discuss your decision tomorrow"
print(f"郵件: '{test_email}' 分類結果 : {classify_email(test_email)}")



