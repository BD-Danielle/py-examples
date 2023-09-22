# ch10_7.py
import itertools
n = {1, 2, 3, 4, 5, 6}
A = set(itertools.combinations(n, 2))
print(f'組合 = {len(A)}')
for a in A:
    print(a)










