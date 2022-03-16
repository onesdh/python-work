# 3-2

# N = 배열의 크기, M = 숫자가 더해지는 횟수, K = 동빈이의 큰 수의 법칙에 따른 결과
# 입력조건

# 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <=10000), K(1 <= 10000)의 자연수가 주어지며,
# 각 자연수는 공백으로 구분한다.

# 둘째 줄에 N 개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는
# 1이상 10000이하의 수로 주어진다.

# 입력으로 주어지는 K는 항상 M보디 작거나 같다.

# 출력조건

# 첫째줄에 동빈이의 큰수의 법칙에 따라 더해진 답을 출력한다.

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
N_list = list(map(int, input().split()))
result = 0

N_list.sort()
print(N_list)

max1 = N_list[N-1]
max2 = N_list[N-2]

while True :
    for i in range(K) :
        if M == 0 :
            break
        result += max1
    if M == 0 :
        break
    result += max2
    M -= 1

print(result)