# question - 20 (valid parenthesis) [EASY]
brackets_string = array1 = input("Enter the parenthesis: ")


def is_valid(s):
    stack = []
    for i in s:
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
        else:
            if i == "}" or i == "]" or i == ")":
                if len(stack) == 0:
                    return False

                removed = stack.pop()
                if (i == "}" and removed != "{") or (i == "]" and removed != "[") or (i == ")" and removed != "("):
                    return False
    return len(stack) == 0


brackets_list = [bracket for bracket in brackets_string]
print(brackets_list)

print(is_valid(brackets_list))
