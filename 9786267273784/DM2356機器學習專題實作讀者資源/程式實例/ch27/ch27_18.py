# ch27_18.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載 iris 數據集
iris = load_iris()
X = iris.data
y = iris.target

# 分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                   test_size=0.2, random_state=42)

# 設定一個儲存所有準確度的列表
accuracy_scores = []

# 迴圈設定 k = 1 到 100, step是 2
k_values = list(range(1, 100, 2))
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)       # 訓練模型
    
    y_pred = knn.predict(X_test)    # 用模型進行預測
    
    # 計算並儲存準確度
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_scores.append(accuracy)    
    print(f'k={k}, 準確度: {accuracy:.3f}')

# 繪製圖表
plt.figure()
plt.plot(k_values, accuracy_scores, marker='o')
plt.title('鳶尾花預估準確度 vs k值')
plt.xlabel('k 值')
plt.ylabel('準確度')
plt.grid(True)
plt.show()
