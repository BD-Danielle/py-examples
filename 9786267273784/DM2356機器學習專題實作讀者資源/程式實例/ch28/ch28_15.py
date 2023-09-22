# ch28_15.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 下載 iris 數據集
iris = load_iris()

X = iris.data  
y = iris.target

# 分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

kernels = ['linear', 'rbf', 'rbf', 'poly']
gamma_values = ['scale', 0.5, 100, 'scale']
titles = ['Linear kernel', 'RBF kernel, gamma=0.5',
          'RBF kernel, gamma=100', 'Poly kernel']

for kernel, gamma, title in zip(kernels, gamma_values, titles):
    model = SVC(kernel=kernel, gamma=gamma, random_state=42)
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    print(f'{title}')
    print(f'訓練資料準確度: {accuracy_score(y_train, y_train_pred):.2f}')
    print(f'測試資料準確度: {accuracy_score(y_test, y_test_pred):.2f}\n')



