# ch32_10.py
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.svm import SVC

# 載入 LFW 數據集
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# 切割訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(
    lfw_people.data, lfw_people.target, test_size=0.2, random_state=42)

# 數據標準化
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 進行PCA降維，保留90%的信息
pca = PCA(n_components=0.9)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 建立與訓練 SVC 模型
svc = SVC(kernel='rbf', random_state=42)
svc.fit(X_train_pca, y_train)

# 在訓練集和測試集上做預測
y_train_pred = svc.predict(X_train_pca)
y_test_pred = svc.predict(X_test_pca)

# 計算並印出訓練集和測試集的準確度
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f"訓練資料集準確度 : {train_accuracy}")
print(f"測試資料集準確度 : {test_accuracy}")

# 列出前20筆數據的實際和預測的標籤
for i in range(20):
    print(f"真實名字: {lfw_people.target_names[y_test[i]]:20s},\
            預測名字: {lfw_people.target_names[y_test_pred[i]]}")



