# ch31_15.py
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Mall_Customers.csv')

# 將性別從文字轉換為數值
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# 根據性別將數據分為兩個子集
male_data = data[data['Gender'] == 0]
female_data = data[data['Gender'] == 1]

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 輸出中文字
# 繪製男性客戶的年收入與消費得分散點圖
plt.scatter(male_data['Annual Income (k$)'],
            male_data['Spending Score (1-100)'],color='blue',label='男性')

# 繪製女性客戶的年收入與消費得分散點圖
plt.scatter(female_data['Annual Income (k$)'],
            female_data['Spending Score (1-100)'],color='red',label='女性')

# 繪製分群結果
plt.title('性別區分 - 年收入 vs 消費力')
plt.xlabel('年收入 Annual Income (k$)')
plt.ylabel('消費力 Spending Score (1-100)')
plt.legend()
plt.show()


