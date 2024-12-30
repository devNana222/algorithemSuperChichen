# 241230 - BubbleSort 

```python
input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))
```

## 문제 분석 
* bubble sort는 다음 배열의 숫자와 현재 배열의 숫자를 비교해서 자리를 바꾸는 방식이다. 
* 한 사이클이 돌고나면 배열의 마지막 자리는 정렬되어있는 상태이므로 마지막 배열을 제외한 앞의 배열들을 비교해줘야한다. 

## 나의 풀이 
```python

def bubble_sort(array):
    i = 0
    j = 0
    array_length = len(array)

    for i in range(array_length -1):
        for j in range(array_length - i - 1):
            if(array[j]>array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array
```

## 더 좋은 방법 
* 파이썬에는 temp 변수를 쓰지 않고도 변경이 가능했다.
```python
 if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
```
유용하게 써질 것 같다. 