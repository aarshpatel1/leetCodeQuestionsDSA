parentheses = input("Enter the parentheses only: ")


def check_parentheses(s):
    for i in range(len(s) - 1):
        if s[i] == "(" and s[i + 1] != ")":
            return False
        elif s[i] == "{" and s[i + 1] != "}":
            return False
        elif s[i] == "[" and s[i + 1] != "]":
            return False

    return True


print(check_parentheses(parentheses))
