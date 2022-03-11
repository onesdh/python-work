# 11-01 배열에서 최솟값 위치를 찾는 함수

def findMinidx(ary) :
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]) :
            minIdx = i
        return minIdx

testAry = [55, 88, 33, 77]
minPos = findMinidx(testAry)
print('최솟값 -->', testAry[minPos])

