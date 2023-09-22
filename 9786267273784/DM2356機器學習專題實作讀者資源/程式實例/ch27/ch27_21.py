# ch27_21.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

# 讀取數據
df = pd.read_csv('nasa.csv')

# 刪除指定的列
df = df.drop(['Name', 'Neo Reference ID', 'Est Dia in M(min)',
              'Est Dia in M(max)', 'Est Dia in Miles(min)',
              'Est Dia in Miles(max)', 'Est Dia in Feet(min)',
              'Est Dia in Feet(max)', 'Epoch Date Close Approach',
              'Relative Velocity km per hr', 'Miles per hour',
              'Miss Dist.(Astronomical)', 'Miss Dist.(lunar)',
              'Miss Dist.(miles)', 'Equinox'],
              axis=1)


# 將 'Hazardous' 列的 True/False 轉換為 1/0
df['Hazardous'] = df['Hazardous'].map({True: 1, False: 0})

# 將 'Close Approach Date' 和 'Orbit Determination Date'
# 轉換為日期時間物件，然後再轉換為時間戳記
df['Close Approach Date'] = pd.to_datetime(df['Close Approach Date'],
                            format='%Y/%m/%d').view('int64') // 10**9
df['Orbit Determination Date'] = pd.to_datetime(df['Orbit Determination Date']).\
                                                view('int64') // 10**9
# 檢查並處理缺失值
if df.isnull().values.any():
    # 你可以選擇填補缺失值，或者丟棄含有缺失值的行，這裡選擇填補中位數
    df.fillna(df.median(), inplace=True)

# 執行 One-hot 編碼
df = pd.get_dummies(df, columns=['Orbiting Body'])

# 分割數據集為特徵和目標
X = df.drop('Hazardous', axis=1)
y = df['Hazardous']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 標準化數據
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 使用KNN演算法進行訓練
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 預測並計算準確度
y_pred = knn.predict(X_test)
print(f'Accuracy : {accuracy_score(y_test, y_pred)}')

# 輸出混淆矩陣
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# 輸出分類報告
print('Classification Report:')
print(classification_report(y_test, y_pred))







