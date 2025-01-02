input = [4, 6, 2, 9, 1]


def selection_sort(array):
    length = len(array)
    i = 0
    j = 0

    for i in range(length-1) :
        new_array = array[i:length]
        m = min(new_array)

        for j in range(len(new_array)) :
            if m == new_array[j] :
                array[i], array[i+j] = array[i+j], array[i]
                break
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))