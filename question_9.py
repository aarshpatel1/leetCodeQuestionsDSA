x = int(input("Enter the number: "))
if x > 0:
    x = str(x)
    n = ""
    for i in range(len(x) - 1, -1, -1):
        n += x[i]

    x = int(x)
    n = int(n)
    print(x)
    print(n)
    if x == n:
        print(True)
    else:
        print(False)
else:
    print(False)

