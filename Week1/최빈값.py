def find_max_occurred_alphabet(string):
    alphabet_array = [0]*26

    for i in string:
        if i.isalpha():
            index = ord(i.lower()) - 97
            alphabet_array[index] += 1

    max_index = alphabet_array.index(max(alphabet_array))
    return chr(max_index + 97)


result = find_max_occurred_alphabet

print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))