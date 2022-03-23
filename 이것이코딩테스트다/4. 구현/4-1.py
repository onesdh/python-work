# 4-1

import sys
input = sys.stdin.readline

N = int(input())

x, y = 1, 1

mo = input().split()

move = ['L', 'R', 'U', 'D']
X = [0, 0, -1, 1]
Y = [-1, 1, 0, 0]

for i in mo :
    for j in range(len(move)) :
        if i == move[j] :
            x_ = x + X[j]
            y_ = y + Y[j]
    if x_ < 1 or y_ < 1 or x_ > N or y_ > N :
        continue
    x, y = x_, y_

print(x,y)