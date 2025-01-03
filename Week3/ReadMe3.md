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


# 250103 - Merge Sort 

```python
array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
    # 이 부분을 채워보세요!
    return

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))
```

## 문제 분석

- merge sort는 정렬되어있는 배열을 합쳐서 정렬하는 방식이다.
- 정렬되어있으므로 각 배열의 맨 앞 수만 비교해서 새로운 배열에 넣어주면 된다.

## 나의 풀이

```python

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

```

## 더 좋은 방법

```python
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1
```

- **시간 복잡도 증가 (`O(n^2)`)**
    - **`pop(0)`의 성능 문제**: 파이썬의 리스트에서 `pop(0)`은 리스트의 맨 앞 요소를 제거한 뒤 나머지 요소를 이동시킨다. 
    - 이 작업은 `O(k)` 시간 복잡도를 가지며, 전체 병합에서 `O((n + m)^2)`로 성능이 저하된다.
    - 중첩 `for` 루프 사용으로 불필요한 비교 연산이 많아, 배열이 클수록 비효율적이다.
- **메모리 비효율성**
    - 매번 `pop(0)`을 호출하며, 원본 배열의 구조를 수정한다. 이는 원본 데이터의 유지가 필요한 상황에서 문제가 된다.
- **복잡한 로직**
    - 중첩 루프와 `pop(0)` 사용으로 코드가 복잡하고 비효율적이다. 추가적인 배열 확장(`extend`) 작업도 필요하다.

# 250103 - Merge Sort2

```python
array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    # 이 곳을 채워보세요!
    return array

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result

print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))
```

## 문제 분석

- 정렬되어있지 않은 배열을 두 배열로 나누어 배열하고 합친다.
- 배열 크기가 1보다 작다는 것은 이미 정렬된 상태임을 의미한다.

```python
def merge_sort(array):
    if len(array)<= 1:
        return array

    mid = len(array)//2
    array1 = array[:mid]
    array2 = array[mid:]

    return merge(merge_sort(array1),merge_sort(array2))

```