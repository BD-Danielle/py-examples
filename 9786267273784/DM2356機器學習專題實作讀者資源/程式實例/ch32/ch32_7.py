# ch32_7.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

digits = datasets.load_digits()

# 分割數據為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(digits.data,
                 digits.target, test_size=0.2, random_state=9)

# 創建PCA物件, n_components表示主成分數量
pca = PCA(n_components=0.6, random_state=9)    # 保留60%的變異性

# 在訓練集上執行PCA
X_train = pca.fit_transform(X_train)

# 在測試集上應用相同的PCA轉換
X_test = pca.transform(X_test)

# 創建決策樹分類器
clf = DecisionTreeClassifier(random_state=9)

# 使用訓練數據來訓練模型
clf.fit(X_train, y_train)

# 預測訓練集和測試集的結果
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

# 計算並輸出訓練集和測試集的準確度
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print('經過 PCA 處理, 保留 60% 變異性的決策樹 DecisionTree 辨識')
print(f'訓練數據的準確度 : {train_accuracy:.3f}')
print(f'測試數據的準確度 : {test_accuracy:.3f}')



