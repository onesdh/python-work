# 10-8 n제곱 계산

tab = ' '
def pow(x, n) :
    global tab
    tab += ' '
    if n == 0 :
        return 1
    print(tab + '{} * {} ^({}-{})'.format(x, x, n, 1))
    return x * pow(x, n-1)

print('2^4')
print('답 -->', pow(2,4))