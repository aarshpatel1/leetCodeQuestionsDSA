# question - 20 (Valid Parentheses)

parentheses = input("Enter the parentheses only: ")


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
    for i in range(len(s) - 1):
        if not check_closing(s[i], i):
            return False
    return True


print(check_parentheses(parentheses))
