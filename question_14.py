# question - 14 (Longest common prefix)

strings = input("Enter the words: ").split(" ")
print(strings)

prefixes = []
for i in range(len(strings)):
    for j in range(i + 1):
        prefixes.append(strings[i][j])

print(prefixes)
