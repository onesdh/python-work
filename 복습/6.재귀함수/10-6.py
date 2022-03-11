# 10-6 별모양 출력을 재귀호출로 구현

def printStar(n) :
    if n > 0 :
        printStar(n-1)
        print("*"*n)

printStar(5)