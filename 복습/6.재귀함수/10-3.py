# 10-3 10부터 1까지의 합계를 재귀호출로 구현

def addNumber(num) :
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))