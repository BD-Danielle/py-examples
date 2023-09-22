# ch23_3_1.py
import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# 加載波士頓房價數據集
print(f"自變數  樣本外形 : {data.shape}")
print(f"目標變數樣本外形 : {target.shape}")

# 輸出第一筆自變數
print("自變數 特徵值")
print(data[0])

# 輸出第一筆目標變數, 房價
print("目標變數 房價")
print(target[0])


