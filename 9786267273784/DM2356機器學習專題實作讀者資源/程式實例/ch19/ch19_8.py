# ch19_8.py
import numpy as np

A = np.matrix([[2, 3], [5, 7]])
B = np.linalg.inv(A)
print(f'A_inv = {B}'.format())
print(f'E     = {(A * B).astype(np.int64)}')





 








