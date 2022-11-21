# @uni_kakurenbo
# https://github.com/uni-kakurenbo/competitive-programming-workspace
#
# CC0 1.0  http://creativecommons.org/publicdomain/zero/1.0/deed.ja

# #language PyPy3 #

from itertools import product
from sys import setrecursionlimit, stderr, argv;
# setrecursionlimit(10**5)
def debug(*args, **opts):
    if argv[-1] == "LOCAL_JUDGE": print(*args, **opts, file=stderr);

n, m = map(int, input().split())

G = [set() for _ in [0] * n]
for _ in [0] * m:
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].add(b); G[b].add(a)

ans = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        ans += any(k in G[i] and k in G[j] for k in range(n))
print(ans)
