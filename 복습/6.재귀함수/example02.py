def sample(n, number) :
    if number < n :
        print(Ary[number], end = ' ' )
    else :
        sample(n, number // n)
        print(Ary[number % n], end = ' ' )

Ary = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

num = int(input('10진수 입력 -->'))
print()
print(' 2진수 : ', end = ' ' )
sample(2, num)
print()
print(' 8진수 : ', end = ' ')
sample(8, num)
print()
print('16진수 : ', end = ' ')
sample(16, num)

