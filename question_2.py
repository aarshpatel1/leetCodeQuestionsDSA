# question - 2 (add two numbers) [MEDIUM]
# there is a problem showing in leetcode but not in local machine that linklist does not find length using len()

array1 = input("Enter the numbers in Array 1: ").split(" ")
array2 = input("Enter the numbers in Array 2: ").split(" ")
answer = []


def int_numbers(array):
    return [int(i) for i in array]


def addTwoNumbers(l1, l2):
    if len(l1) != len(l2):
        add_zeros = len(l1) - len(l2)
        if add_zeros > 0:
            for i in range(add_zeros):
                l2.append(0)
        else:
            for i in range(add_zeros):
                l1.append(0)

    sum_array = []
    reminder = 0
    addition = 0
    for i in range(len(l1)):
        total_of_2_numbers = l1[i] + l2[i] + addition
        if total_of_2_numbers >= 10:
            addition = 0
            reminder = total_of_2_numbers % 10
            sum_array.append(reminder + addition)
            addition += 1
            reminder = 0
        else:
            sum_array.append(total_of_2_numbers)

    if addition != 0 and sum_array[-1] == 0:
        sum_array.append(addition)

    return sum_array


array1 = int_numbers(array1)
array2 = int_numbers(array2)

print(array1)
print(array2)

print(addTwoNumbers(array1, array2))

# print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
# print(addTwoNumbers([0], [0]))
# print(addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
