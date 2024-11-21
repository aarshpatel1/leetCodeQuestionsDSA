# question - 14 (Longest common prefix) [EASY]

words = input("Enter the words: ").split(" ")
print(words)


def check_prefix(prefix_array):
    is_same = True
    for k in range(len(prefix_array) -1):
        if k + 1 < len(prefix_array):
            if prefix_array[k] != prefix_array[k + 1]:
                return False

    return is_same


def common_prefix(strings):
    final_prefix = ""
    smallest_string = min(len(word) for word in strings)
    print(smallest_string)

    for j in range(smallest_string):
        prefix_chars = []
        for i in range(len(strings)):
            prefix_chars.append(strings[i][j])
        if not check_prefix(prefix_chars):
            break
        else:
            final_prefix += prefix_chars[0]

    return final_prefix

print(common_prefix(words))