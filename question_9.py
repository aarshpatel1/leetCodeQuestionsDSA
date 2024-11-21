# question - 9 (check palindrome number) [EASY]

number = int(input("Enter the number: "))


def is_palindrome(x):
    if x == 0:
        return True
    elif x > 0:
        x = str(x)
        n = ""
        for i in range(len(x) - 1, -1, -1):
            n += x[i]

        x = int(x)
        n = int(n)
        print(x)
        print(n)
        if x == n:
            return True
        else:
            return False
    else:
        return False


print(is_palindrome(number))
