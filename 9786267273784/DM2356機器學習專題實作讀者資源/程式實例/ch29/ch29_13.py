# ch29_13.py
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 從sklearn的datasets中讀取新聞數據集
newsgroups_train = fetch_20newsgroups(subset='train')

# 建立一個pipeline, 包含TfidfVectorizer和MultinomialNB
pipeline = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB(alpha=.1)
)

# 使用訓練數據訓練模型
pipeline.fit(newsgroups_train.data, newsgroups_train.target)

# 定義我們要分類的文件
text = ['''
    Baseball is a bat-and-ball game played between two opposing teams
    who take turns batting and fielding. The game proceeds when a player
    on the fielding team, called the pitcher, throws a ball which a
    player on the batting team tries to hit with a bat. 
    ''', 
    '''
    While the study of space is carried out mainly by astronomers with
    telescopes, the physical exploration of space is conducted both by
    uncrewed robotic space probes and human spaceflight. Space
    exploration, like its classical form astronomy, is one of the main
    sources for space science.
    ''']

# 將本件轉換為數字特徵向量，並進行預測
predicted = pipeline.predict(text)

# 輸出預測結果
for doc, category in zip(text, predicted):
    print('文件內容')
    print(f"{doc}\n分類 -> {newsgroups_train.target_names[category]}\n")



