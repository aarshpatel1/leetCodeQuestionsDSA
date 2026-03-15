# question 7 (reverse integer)

def reverse_number(x):
    is_negative = False
    if x <0:
        x*=-1
        is_negative = True

    new_num=x
    length=1
    while x>0:
        length*=10
        # print(x%10)
        x//=10

    length//=10
    reversed_number =0
    while length>0:
        reversed_number += (new_num%10 )* length
        new_num//=10
        length //= 10

    # print("================")
    # print(length)
    # print("================")
    if reversed_number < -2147483648 or reversed_number >  2147483647:
        return 0

    if is_negative:
        reversed_number *= -1

    return reversed_number

# number = int(input("Enter the number: "))
# print(reverse_number(number))
print(reverse_number(123))
print(reverse_number(5324))
print(reverse_number(-653))
print(reverse_number(210))
print(reverse_number(1534236469))

