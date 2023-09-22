# ch29_18.py
import jieba

text = '我最喜歡的學校是台塑企業集團的明志工專'
words = ' '.join(jieba.cut(text))
print(type(words))
print(words)








