input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_array = [0]*26

    for i in string:
        index = ord(i) - 97
        alphabet_array[index] += 1

    non_repeat_array = []
    for j in range(len(alphabet_array)):
        alphabet_array[j] = alphabet_array[j]

        if alphabet_array[j] == 1:
            non_repeat_array.append(chr(97 + j))

    for c in string:
        if c in non_repeat_array:
            return c
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))