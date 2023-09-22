# ch10_5.py
import itertools
n = {1, 2, 3, 4, 5}
A = set(itertools.product(n, n, n))
print(f'排列方式 = {len(A)}')
for a in A:
    print(a)










