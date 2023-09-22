# ch25_4.py
from joblib import load
from sklearn import tree
from graphviz import Source

dtc = load('dtc3.joblib')       # 開啟max_depth=3的決策樹模型

graph = Source(tree.export_graphviz(dtc, out_file=None))
graph.format = 'png'
graph.render(filename='dtc_tree', view=True)









