# question - 392 (Is Subsequence) [EASY] result = 

def is_subsequence(s, t):
    if len(s) == len(t) and s != t:
        return False

    if len(s) > len(t):
        return False

    for i in s:
        if i not in t:
            return False

    t = list(t)

    subsequence_char_index = []

    for i in s:
        for j in t:
            if i == j:
                subsequence_char_index.append(j)
                t.remove(j)
                print(t)
                print(subsequence_char_index)
                break


    subsequence_char_index= "".join(subsequence_char_index)

    if subsequence_char_index!= s:
        return False

    return True


t = input("Enter the string: ")
s = input("Enter the subsequence: ")

result = is_subsequence(s=s, t=t)

print(result)
