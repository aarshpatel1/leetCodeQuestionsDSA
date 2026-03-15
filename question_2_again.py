# question 2 (Add Two Numbers) [medium]
def add_two_numbers(l1, l2):
    print(l1)
    print(l2)

    l1_length = len(l1)
    l2_length = len(l2)

    length_difference = l1_length - l2_length
    if length_difference > 0:
        for i in range(length_difference):
            l2.append(0)

    carry = 0
    result = []
    for i in range(l1_length):
        result.append(l1[i] + l2[i] + carry)
        carry = 0
        if result[i] >= 10:
            result[i] %= 10
            carry = 1

    if carry != 0:
        result.append(carry)

    return result


print(add_two_numbers([2, 4, 3], [5, 6, 4]))
print("=========================")
print(add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))


# def add_two_numbers(l1, l2):
#     print(l1)
#     print(l2)
#
#     def count_length(given_list):
#         length = 0
#         for _ in given_list:
#             length += 1
#         return length
#
#     l1_length = count_length(l1)
#     l2_length = count_length(l2)
#
#     length_difference = l1_length - l2_length
#     if length_difference > 0:
#         for i in range(length_difference):
#             l2.append(0)
#
#     carry = 0
#     result = []
#     for i in range(l1_length):
#         result.append(l1[i] + l2[i] + carry)
#         carry = 0
#         if result[i] >= 10:
#             result[i] %= 10
#             carry = 1
#
#     if carry != 0:
#         result.append(carry)
#
#     return result
#
#
# print(add_two_numbers([2, 4, 3], [5, 6, 4]))
# print("=========================")
# print(add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
