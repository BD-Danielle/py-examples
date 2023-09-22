# ch10_3.py
import itertools
n = {'A', 'B', 'C', 'D', 'E'}
r = 5
A = set(itertools.permutations(n, r))
print(f'業務員路徑數 = {len(A)}')
for a in A:
    print(a)










