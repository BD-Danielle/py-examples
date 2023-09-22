# ch33_12.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# 讀取數據集
data = pd.read_csv('oldfaithful.csv')

# 將特徵進行標準化
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 繪製4個子圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

clusters = [2, 3, 4, 5]
for i, ax in enumerate(axs.flat):
    # 進行凝聚分群
    cluster = AgglomerativeClustering(n_clusters=clusters[i])
    data['class'] = cluster.fit_predict(data_scaled)

    # 繪製散點圖，不同顏色表示不同的分群
    for c in range(clusters[i]):
        ax.scatter(data[data['class'] == c]['Eruptions'], 
                   data[data['class'] == c]['Waiting'], 
                   label=f'Cluster {c+1}')
    
    ax.set_title(f'Old Faithful數據 - 凝聚分群 - 群集數 : {i+2}')
    ax.set_xlabel('爆發持續時間Eruptions(分鐘)')
    ax.set_ylabel('等待時間Waiting(分鐘)')
    ax.legend()

plt.subplots_adjust(wspace=0.2, hspace=0.4)
plt.show()
