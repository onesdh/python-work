# 10-4 5!를 재귀호출로 구현

def factorial(num) :
    if num <= 1 :
        print("1반환")
        return 1
    print("{} * {}! 호출".format(num, num-1))
    retVal = factorial(num-1)

    print("{} * {}! = ({}) 호출".format(num, num-1, retVal))
    return num*retVal

print('\n 5! = ', factorial(5))