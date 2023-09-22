# ch10_6.py
import itertools
n = {1, 2, 3, 4, 5}
A = set(itertools.combinations(n, 3))
print(f'組合 = {len(A)}')
for a in A:
    print(a)










