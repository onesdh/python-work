# 12-3 퀵 정렬의 간단한 구현

def quickSort(ary) :
    n = len(ary)
    if n <= 1 :
        return ary
    pivot = ary[n//2]
    leftAry, rightAry = [], []

    for num in ary :
        if num < pivot :
            leftAry.append(num)
        elif num > pivot :
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

print('정렬 전-->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)