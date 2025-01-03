array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array = []
    len1 = len(array1)
    len2 = len(array2)

    for i in range(len1):
        for j in range(len2):
            if len(array2) == 0:
                break
            if array1[0] < array2[0]:
                array.append(array1.pop(0))
                break
            elif array1[0] > array2[0]:
                array.append(array2.pop(0))
            else:
                array.append(array1.pop(0))
                array.append(array2.pop(0))

    array.extend(array1)
    array.extend(array2)
    return array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))