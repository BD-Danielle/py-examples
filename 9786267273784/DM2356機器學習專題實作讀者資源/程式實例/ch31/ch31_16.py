# ch31_16.py
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Mall_Customers.csv')

# 根據年齡將客戶分成不同的年齡層
bins = [18, 25, 35, 55, data['Age'].max()]
labels = ['年青人(18~25)', '青年成人(26~35)',
          '中年人(36~55)', '高年齡生(56以上)']
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels)

# 繪製每個年齡層的年收入與消費得分散點圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
for age_group in labels:
    plt.scatter(data[data['Age Group'] == age_group]['Annual Income (k$)'], 
                data[data['Age Group'] == age_group]['Spending Score (1-100)'], 
                label=age_group)

plt.title('年齡層區分 - 年收入 vs 消費力')
plt.xlabel('年收入 Annual Income (k$)')
plt.ylabel('消費力 Spending Score (1-100)')
plt.legend()
plt.show()
