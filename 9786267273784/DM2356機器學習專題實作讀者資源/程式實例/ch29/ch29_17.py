# ch29_17.py
import jieba

text = '我最喜歡的學校是台塑企業集團的明志工專'
words = jieba.cut(text)
print(type(words))
for word in words:
    print(word)





