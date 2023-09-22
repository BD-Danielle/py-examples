# ch29_20.py
import jieba
positive_words = ['好', '喜歡', '棒', '驚人', '超棒']
negative_words = ['差', '討厭', '糟', '失望', '糟糕']

def sentiment_analysis(comment):
    pos_count = 0
    neg_count = 0
    for word in jieba.cut(comment):
        if word in positive_words:
            pos_count += 1
        elif word in negative_words:
            neg_count += 1

    if pos_count + neg_count == 0:
        return "無法判斷情感"
    elif pos_count > neg_count:
        return "正面評價"
    else:
        return "負面評價"

comment = "這部電影真的太糟糕了, 我很失望"
print(f'{comment} : {sentiment_analysis(comment)}')

comment = "這部電影超棒的, 我很喜歡"
print(f'{comment} : {sentiment_analysis(comment)}')


