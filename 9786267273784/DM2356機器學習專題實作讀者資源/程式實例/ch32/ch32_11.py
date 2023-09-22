# ch32_11.py
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# 載入 LFW 數據集
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# 切割訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(
    lfw_people.data, lfw_people.target, test_size=0.2, random_state=42)

# 數據標準化
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 一組預先定義好的 PCA 的 n_components 值
components = [0.5, 0.6, 0.7, 0.8, 0.9]
train_accuracies = []
test_accuracies = []

for component in components:
    # 進行PCA降維
    pca = PCA(n_components=component, whiten=True)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)

    # 建立與訓練 SVC 模型
    svc = SVC(kernel='rbf', random_state=42)
    svc.fit(X_train_pca, y_train)

    # 在訓練集和測試集上做預測並計算準確度
    y_train_pred = svc.predict(X_train_pca)
    y_test_pred = svc.predict(X_test_pca)
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

# 繪製結果
plt.figure(figsize=(10, 6))
plt.plot(components, train_accuracies, marker='o', label='Training Accuracy')
plt.plot(components, test_accuracies, marker='o', label='Test Accuracy')
plt.title('Accuracy vs PCA Components')
plt.xlabel('PCA Components')
plt.ylabel('Accuracy')
plt.legend()
plt.grid()
plt.show()



