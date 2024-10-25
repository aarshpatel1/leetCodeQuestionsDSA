# question - 20 (Valid Parentheses)

parentheses = input("Enter the parentheses only: ")

parentheses = [i for i in parentheses]


def check_closing(opening, index):
    if opening == "(":
        closing = ")"
    elif opening == "{":
        closing = "}"
    elif opening == "[":
        closing = "]"
    else:
        return True
    for j in range(index, len(parentheses)):
        if parentheses[j] == closing:
            return True
    return False


def check_parentheses(s):
    openings = ["(", "{", "["]
    closings = [")", "}", "]"]
    if len(s) == 1 or s[0] in closings:
        return False
    else:
        for i in range(len(s) - 1):
            if s[i] in openings and s[i + 1] in closings:
                if openings.index(s[i]) != closings.index(s[i + 1]):
                    return False
            else:
                if not check_closing(s[i], i):
                    return False
    return True


print(check_parentheses(parentheses))
