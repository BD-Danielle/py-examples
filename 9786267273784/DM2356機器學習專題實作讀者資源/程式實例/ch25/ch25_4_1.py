# ch25_4_1.py
from joblib import load
from sklearn.tree import export_graphviz
from sklearn.datasets import load_wine

wine = load_wine()
dtc = load('dtc3.joblib')       # 開啟max_depth=3的決策樹模型
with open("wine.dot", "w") as file:
    file = export_graphviz(dtc,
                        feature_names=wine.feature_names[:2],
                        out_file=file)








