a, b = map(int,input().split())

def add(num1, num2) :
    if num1 > num2 :
        if num1 <= num2 :
            return num2
        return num1 + add(num1-1, num2)

    else :
        if num2 <= num1:
            return num1
        return num2 + add(num1, num2-1)

print(add(a,b))