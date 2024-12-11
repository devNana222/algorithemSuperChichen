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
