# question - 1 (find the index of numbers which total is equal to target) [EASY]

array = input("Enter the numbers: ").split(" ")
number = [int(i) for i in array]
target = int(input("Enter the total you want: "))
answer = []

for i in range(len(number)):
    if not answer:
        for j in range(len(number)):
            if i != j:
                if number[i] + number[j] == target:
                    answer.extend([i, j])
                    break

print(answer)

