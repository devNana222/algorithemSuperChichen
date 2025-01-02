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

# 250102 - SelectionSort 
```python
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))
```

## 문제 분석 
* 선택 정렬은 모든 배열을 훑은 뒤 가장 작은 숫자를 찾아 정렬 되지 않은 가장 앞쪽의 수와 자리를 바꾸는 정렬이다. 
* 결국 모든 정렬을 훑어야 하므로 이중 for문을 사용할 수 밖에 없다. 
* 정렬된 배열 이후만 보면된다. 

## 나의 풀이 
```python

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
```

## 더 좋은 풀이 
```python
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):  # i 이후 범위를 탐색
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 최솟값과 교환
    return array

```

* `min()`은 추가적인 메모리를 사용한다. 
* `new_array = array[i:length]`는 배열을 매번 슬라이싱하며 새로운 배열을 생성한다. 
* 이는 메모리 사용량을 증가시키고 실행 시간을 늘린다.

# 250102 - Insert Sort 

```python
input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 이 부분을 채워보세요!
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))
```

## 문제 분석 
* 삽입 정렬은 정렬 되지 않은 요소가 정렬된 배열을 뒤에서부터 다시 탐색한다. 


```python

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

```
## 실패 
`for j in range(i)`가 잘못되었다. 
* `range()` 의 범위에 대한 이해가 부족해서 오래 걸렸다. 
* 이미 정렬된 상태이므로 한번 변경하고 나면 변경할 필요가 없는데 break를 해주지 못했다. 
