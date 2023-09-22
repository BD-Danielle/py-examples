# ch25_8.py
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from graphviz import Source

# 讀取Seaborn中的titanic數據集
titanic_data = sns.load_dataset('titanic')

# 數據預處理
titanic_data = titanic_data[['survived', 'pclass', 'sex']]

# 將 sex 變數轉換為數字編碼
sex_encoder = LabelEncoder()
sex_encoded = sex_encoder.fit_transform(titanic_data['sex'])
titanic_data['sex'] = sex_encoded

# 分割數據為訓練集和測試集
X = titanic_data.drop('survived', axis=1)
y = titanic_data['survived']
X_train,X_test,y_train,y_test = train_test_split(X,y,
                                test_size=0.2,random_state=5)

# 建立決策樹模型
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)

# 進行預測
y_pred = dt_classifier.predict(X_test)
print(f"測試的真實分類\n{np.array(y_test)}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("="*70)

# 評估模型
print(f"準確率(Accuracy Score):{accuracy_score(y_test,y_pred):.2f}")

# 交叉分析
pred_rate = dt_classifier.predict_proba(X_test)
print(pd.crosstab(pred_rate[:,0], columns=[X_test['pclass'],
                                           X_test['sex']]))

# 繪製決策樹
graph = Source(tree.export_graphviz(dt_classifier, out_file=None))
graph.format = 'png'
graph.render(filename='dt_classifier_tree', view=True)






