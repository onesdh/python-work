# 12-4 퀵 정렬의 간단한 구현(중복된 값을 고려)

def quickSort(ary) :
    n = len(ary)
    if n <= 1 :
        return ary
    
    pivot = ary[n // 2]
    leftAry, midAry, rightAry = [], [], []

    for num in ary :
        if num < pivot :
            leftAry.append(num)
        elif num > pivot :
            rightAry.append(num)
        else :
            midAry.append(num)

    return quickSort(leftAry) + midAry + quickSort(rightAry)

dataAry = [120, 120, 188, 150, 168, 50, 50, 162, 105, 120, 177, 50]

print('정렬 전-->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)