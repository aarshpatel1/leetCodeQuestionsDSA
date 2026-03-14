# question - 3 (longest substring without repeating characters)

s = input("Enter the string: ")


def length_of_longest_substring(s):
    empty_string = ""
    for i in s:
        if i not in empty_string:
            empty_string += i
        else:
            empty_string = ""

    return empty_string


print(length_of_longest_substring(s=s))
