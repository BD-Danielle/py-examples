# ch28_17.py
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 載入數據集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 切分數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=9)

# 特徵縮放 - 標準化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

kernels = ['linear', 'rbf', 'poly']

for kernel in kernels:
    # 建立 SVM 分類器
    clf = SVC(kernel=kernel, C=1)

    # 訓練模型
    clf.fit(X_train, y_train)

    # 預測訓練集和測試集
    y_train_pred = clf.predict(X_train)
    y_test_pred = clf.predict(X_test)

    # 計算 accuracy
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)
    print(f"使用 '{kernel}' 核函數")
    print(f"訓練數據的準確率 : {train_acc:.3f}")
    print(f"測試數據的準確率 : {test_acc:.3f}")
    print("-"*70)


