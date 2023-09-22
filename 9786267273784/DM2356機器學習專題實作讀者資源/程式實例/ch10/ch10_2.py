# ch10_2.py
import itertools
n = {'a', 'b', 'c', 'd', 'e'}
r = 2
A = set(itertools.permutations(n, r))
print(f'基因配對組合數量 = {len(A)}')
for a in A:
    print(a)










