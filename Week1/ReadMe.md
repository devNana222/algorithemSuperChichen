# 241210 - 최대값

## 문제
```python
def find_max_num(array):
    # 이 부분을 채워보세요!
    return 1


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
```

## 문제 분석 
* 최대값 저장하는 변수 선언하기
* 최대값 변수와 다음에 오는 숫자들을 비교해서 더 큰값은 최대값 변수로 저장하기

*** 
# 241211 - 최빈값

## 문제 
```python
def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    return "a"


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
```

## 유용한 함수
`str.isalpha()` : 해당 문자열이 알파벳인지 확인할 수 있다. 
`ord()` : 하나의 문자를 인자로 받고 해당하는 문자에 해당하는 유니코드 정수 반환 
`chr()` : 하나의 정수를 인자로 받고 정수에 해당하는 유니코드 문자 반환
*** 
# 241212 - 점근표기법 

## 문제 
```python
def is_number_exist(number, array):
    for element in array:
        if number == element:
            return True
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3,[3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7,[6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2,[6,9,2,7,1888]))
```

## 문제 분석
    - array를 for문으로 돌며 원소 하나씩 비교하기
    - 운 좋으면 첫트만에 찾고(1) / 안 좋으면 배열 끝까지 찾는다(N)
    - for문 안에서 바로 return을 함으로써 불필요한 코드를 제거한다.

# 241212 - 곱하기

## 문제 
```python
def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    return 1


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))
```

## 문제분석 

    - 숫자는 0을 포함한 양의 정수로 이루어 져 있다.
    - 0과 1은 무조건 더하는게 더 큰 결과를 낼 수 있다.
    - 0과 1이 아니라면 곱한다.

# 241212 - 반복되지않는 문자 

## 문제 
```python

input = "abadabac"

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
```

## 문제분석
    - 전체 string을 하나하나 보면서 저장함
    - 알파벳 순서의 배열에 따라 수를 추가함
    - 알파벳 배열을 돌면서 카운트가 1인 알파벳을 찾는다 > 배열로만들기
    - 최빈값 1인 알파벳 배열과 string을 비교하며 제일 먼저 찾은 알파벳을 반환한다.
## 잘못 생각한 것
    
    지난번 최빈값 하는 방식으로 하면 될거라 생각했는데 간과한게 있었다… 
    
    `print("정답 = d 현재 풀이 값 =", result("abadabac"))` 여기서 바로 알았는데
    
    d는 c보다 ascii code가 크다. 
    
    그래서 제일 처음 나오는 반복되지 않는 수를 찾는 것임에도 d가 아닌 c가 나온다.