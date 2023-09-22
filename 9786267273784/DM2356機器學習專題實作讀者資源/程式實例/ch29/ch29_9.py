# ch29_9.py
from sklearn.datasets import fetch_20newsgroups

# 下載並載入20newsgroups數據集
newsgroups = fetch_20newsgroups(subset='all')

# 顯示數據集的大小
print("數據集大小：", len(newsgroups.data))

# 顯示所有新聞組的名字
print("新聞組名字：", newsgroups.target_names)

# 顯示第一條新聞的內容
print("\n第一條新聞的內容：\n", newsgroups.data[0])

# 顯示第一條新聞的標籤（即新聞組的索引）
print("第一條新聞的標籤：", newsgroups.target[0])

# 顯示第一條新聞的標籤對應的新聞組名字
print("\n第一條新聞的新聞組名字 : ", end='')
print(newsgroups.target_names[newsgroups.target[0]])


