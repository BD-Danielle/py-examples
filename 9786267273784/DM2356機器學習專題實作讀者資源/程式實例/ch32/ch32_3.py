# ch32_3.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 載入Iris數據集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 標準化特徵
sc = StandardScaler()
X = sc.fit_transform(X)

# 使用PCA降維
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 切分數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X_pca, y,
                                   test_size=0.2, random_state=42)

# 建立一個SVM分類器
clf = SVC(kernel='linear', random_state=42)
clf.fit(X_train, y_train)

# 預測測試集
y_pred = clf.predict(X_test)

# 輸出準確度
print(f"準確度 : {accuracy_score(y_test, y_pred)}")

# 繪製決策邊界
x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.6)

# 繪製散點圖
plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], color='red',
            label=iris.target_names[0])
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], color='blue',
            label=iris.target_names[1])
plt.scatter(X_pca[y == 2, 0], X_pca[y == 2, 1], color='green',
            label=iris.target_names[2])
plt.legend()    # 圖例
plt.show()


