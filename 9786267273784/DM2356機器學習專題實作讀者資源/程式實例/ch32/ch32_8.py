# ch32_8.py
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt

# 下載 LFW 數據集
lfw_people = fetch_lfw_people(resize=0.4)

# 資料集的基本資訊
n_samples, h, w = lfw_people.images.shape
n_features = lfw_people.data.shape[1]
n_classes = len(lfw_people.target_names)

print(f"圖片數量     : {n_samples}")
print(f"圖片特徵數量 : {n_features}")
print(f"標籤數量     : {n_classes}")
print(f"LFW描述\n{lfw_people.DESCR}")

# 顯示前 10 張圖片
fig, ax = plt.subplots(3, 5, figsize=(12, 9))

for i, axi in enumerate(ax.flat):
    axi.imshow(lfw_people.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[],
            xlabel=lfw_people.target_names[lfw_people.target[i]])

plt.show()


