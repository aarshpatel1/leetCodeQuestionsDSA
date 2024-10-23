# question - 4 (find the median of 2 arrays)
array1 = input("Enter the numbers in Array 1: ").split(" ")
array2 = input("Enter the numbers in Array 2: ").split(" ")


def int_numbers(array):
    return [int(i) for i in array]


array1 = int_numbers(array1)
array2 = int_numbers(array2)


# ================== write your code below ================== #
def find_median_sorted_arrays(nums1, nums2):
    merged_array = nums1 + nums2
    merged_array.sort()
    print(merged_array)
    array_len = len(merged_array)
    if array_len % 2 == 0:
        return (merged_array[array_len // 2] + merged_array[array_len // 2 - 1]) / 2
    else:
        return merged_array[array_len // 2]


# ================== write your code above ================== #

print(find_median_sorted_arrays(array1, array2))
