# 10-7 구구단
def gugu(dan, num) :
    print('{} x {} = {}'.format(dan, num, dan*num))
    if num < 9 :
        gugu(dan, num +1)

for dan in range(2, 10) :
    print('## {}단 ##'.format(dan))
    gugu(dan, 1)