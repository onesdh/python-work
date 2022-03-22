# 3-3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = 0

for i in range(N) :
    card = list(map(int, input().split()))
    n_min = min(card)

    result = max(n_min, result)

print (result)