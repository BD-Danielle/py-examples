# ch24_12.py
import pandas as pd
import matplotlib.pyplot as plt

# 讀取糖尿病數據集
df = pd.read_csv('diabetes_new.csv')

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.hist(df['Glucose'], bins=10, edgecolor='black')
plt.xlabel('血糖值 Glucose')
plt.ylabel('人數 Frequency')
plt.title('血糖分佈 Distribution of Glucose')
plt.show()



