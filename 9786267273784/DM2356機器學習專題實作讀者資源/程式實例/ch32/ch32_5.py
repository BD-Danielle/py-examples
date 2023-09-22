# ch32_5.py
from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

# 選擇前10個數字顯示
fig = plt.figure(figsize=(10, 4))

for i in range(10):
    # 2x5的子圖, 第i+1個
    ax = fig.add_subplot(2, 5, i + 1)
    # 顯示圖片, 使用二值色彩映射
    ax.imshow(digits.images[i], cmap=plt.cm.binary)
    # 在上方添加真實標籤作為標題
    ax.set_title('Label: %s' % digits.target[i])
    # 隱藏座標軸
    plt.axis('off')

# 顯示結果
plt.tight_layout()
plt.show()

