# 241223 - 이진탐색
```python
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
```

- 문제 분석
    - 절반이 되는 지점을 찾는다(배열 (length-1 )//2)
        - ex) length가 13이라면 0~6이 절반일 것 .
    - 값을 찾을 때 까지, 배열을 더이상 쪼갤 수 없을 때 까지 쪼개며 찾는다.
    
- 잘못 생각한 것
    - 재귀호출을 통해 새로운 배열을 호출하는 방식을 생각했다.
    
    ```python
    finding_target = 17
    finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    
    def is_existing_target_number_binary(target, array):
        if len(array) < 2 :
            return False
        else :
            if target == array[(len(array)-1)//2]:
                return True
            elif target > array[(len(array)-1)//2] :
                return is_existing_target_number_binary(target, array[(len(array)-1)//2: len(array)])
            elif target < array[(len(array)-1)//2] :
                return is_existing_target_number_binary(target, array[0: (len(array)-1)//2+1])
            else :
                return False
    
    result = is_existing_target_number_binary(finding_target, finding_numbers)
    print(result)
    ```
    

하지만 `finding_target` 을 변경하니 오류가 났다. 

이유는 

- **타겟을 찾을 수 없는 경우를 처리하지 않음**
    - 배열의 길이가 1이 되거나 배열에 타겟이 없을 때도 재귀 호출이 계속되어 불필요한 연산이 발생할 수 있습니다.
- **중앙값 계산 오류**
    - `(len(array) - 1) // 2`를 사용해 배열의 중간 인덱스를 계산하지만, 정확한 이진 탐색을 위해서는 그냥 `len(array) // 2`를 사용하는 것이 더 간단하고 정확합니다.
- **재귀 호출의 슬라이싱 문제**
    - Python에서 슬라이싱(`array[start:end]`)은 새로운 배열을 생성하므로, 배열이 커질수록 메모리 효율이 떨어지고 성능 저하를 초래합니다.
- **배열이 정렬된 상태라고 가정하지 않음**
    - 이진 탐색은 배열이 정렬되어 있어야만 작동합니다. 입력 배열이 정렬되지 않은 경우 올바르게 동작하지 않습니다.

⇒ 사실 재귀호출의 방법도 틀린건 아니라고 생각했지만 “재귀 호출의 슬라이싱 문제” 에서 이 코드는 올바르지 않은 코드라고 판단이 되었다. 

- 결과코드
    
    ```python
    finding_target = 14
    finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    
    def is_existing_target_number_binary(target, array):
     
        start = 0
        end = len(array) - 1
    
        while(start <= end):
            mid = (start + end) // 2
            if(array[mid] == target):
               return True
            elif(array[mid] > target):
               end = mid - 1
            else :
               start = mid + 1
    
        return False
    
    result = is_existing_target_number_binary(finding_target, finding_numbers)
    print(result)
    ```