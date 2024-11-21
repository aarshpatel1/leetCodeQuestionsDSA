# question - 2 [NOT COMPLETED YET]
array1 = input("Enter the numbers in Array 1: ").split(" ")
array2 = input("Enter the numbers in Array 2: ").split(" ")
answer = []


def int_numbers(array):
    return [int(i) for i in array]


def reverse_array(array):
    new_array = []
    for n in range(len(array) - 1, -1, -1):
        new_array.append(array[n])
    return new_array


def count_extra(n):
    count = 0
    while n >= 10:
        n -= 10
        count += 1
    return count


count_extra(42)

array1 = int_numbers(array1)
array1 = reverse_array(array1)

array2 = int_numbers(array2)
array2 = reverse_array(array2)

print(array1)
print(array2)

if len(array1) == len(array2):
    for i in range(len(array1)):
        if array1[i] + array2[i] < 10:
            answer.append(array1[i] + array2[i])
        else:
            calculation = array1[i] + array2[i] - count_extra(array1[i] + array2[i])
            answer.append(calculation)

print(answer)
