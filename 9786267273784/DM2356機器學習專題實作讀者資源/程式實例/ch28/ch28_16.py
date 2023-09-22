# ch28_16.py
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# 載入數據集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 切分數據集為訓練集和測試集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,
                                                 random_state=9)

# 特徵縮放
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立 SVM 分類器, 訓練模型
clf = SVC(kernel='linear', C=1)
clf.fit(X_train, y_train)

# 預測測試集
y_pred = clf.predict(X_test)
print(f"測試的真實值\n{y_test}")
print("-"*70)
print(f"預測的目標值\n{y_pred.round(1)}")
print("-"*70)

# 計算 accuracy
acc = accuracy_score(y_test, y_pred)
print(f"準確率(Accuracy Score) : {acc:.3f}")
print("-"*70)

# 生成分類報告
report = classification_report(y_test, y_pred)
print("分類報告(Classification Report):")
print(report)

