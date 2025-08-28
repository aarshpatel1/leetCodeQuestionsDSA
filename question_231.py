# question - 231 (Power of 2) [EASY] result = 3ms beats 14.40% of python3 submissions

def isPowerOfTwo(n):
    print(n)
    power = 0
    if n == 1:
        return True
    elif n % 2 == 0:
        max = 0
        while max != 31:
            if pow(2, max) == n:
                return True
            max += 1
        return False
    else:
        return False


print(isPowerOfTwo(3))
