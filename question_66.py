# question - 66 (Plus One) [EASY] result = 100%

def plusOne(digits):
    # print(digits)
    string_of_digits = ""
    for i in digits:
        string_of_digits += str(i)
    # print(string_of_digits)
    # print(type(string_of_digits))
    number_from_string = int(string_of_digits) + 1
    # print(number_from_string)
    number_in_array = []
    while number_from_string > 0:
        single_int = number_from_string % 10
        number_in_array.append(single_int)
        number_from_string = number_from_string // 10

    # print(number_in_array[::-1])
    return number_in_array[::-1]


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
