# question - 27 (remove element) [EASY] result = 100%

numbers = input("Enter the numbers: ").split(" ")
remove_value = int(input("Enter the removing value: "))

int_numbers = [int(i) for i in numbers]


def remove_element(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = "_"
            count += 1
    print(nums)
    for i in nums:
        if str(i) == "_":
            nums.remove("_")
            nums.append("_")
    print(nums)
    return len(nums) - count


print(remove_element(int_numbers, remove_value))
