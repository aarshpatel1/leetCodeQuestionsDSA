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
    openings = ["(", "{", "["]
    closings = [")", "}", "]"]
    if len(s) == 1 or s[len(s) - 1] in openings:
        return False
    else:
        for i in range(len(s) - 1):
            if s[i] == "(" and s[i + 1] != ")" and s[i + 1] in closings:
                return False
            elif s[i] == "{" and s[i + 1] != "}" and s[i + 1] in closings:
                return False
            elif s[i] == "[" and s[i + 1] != "]" and s[i + 1] in closings:
                return False
            else:
                if not check_closing(s[i], i):
                    return False

        return True


print(check_parentheses(parentheses))
