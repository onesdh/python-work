# 10-5 카운트다운을 재귀함수로 구현

def countDown(n) :
    if n == 0 :
        print("발사")
    else :
        print(n)
        countDown(n-1)

countDown(5)