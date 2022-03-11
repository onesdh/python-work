from typing import Counter


def openBox() :
    global count
    print("종이상자를 엽니다")
    count -= 1
    if count == 0 :
        print("**반지를 넣고 반환합니다.")
        return
    openBox()
    print("종이상자를 닫습니다")

count = 10
openBox()