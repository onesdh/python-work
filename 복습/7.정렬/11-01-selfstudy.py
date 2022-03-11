# 11-01-selfstudy 배열에서 최대값 위치를 찾는 함수

def findMaxidx(ary) :
    maxIdx = 0
    for i in range(1, len(ary)):
        if (ary[maxIdx] < ary[i]) :
            maxIdx = i
        return maxIdx

testAry = [55, 88, 33, 77]
minPos = findMaxidx(testAry)
print('최댓값 -->', testAry[minPos])