# question - 13 (Roman to Integer)

roman = input("Enter the Roman Number: ").upper()


# method - 1
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

valid_number = True
for i in roman:
    if i not in values:
        valid_number = False
        break

roman += "N"
integer_number = 0
print(roman)

i = 0
if valid_number:
    # for i in range(len(roman)):
    while i <= (len(roman) - 1):
        if roman[i] == "D":
            integer_number += values["D"]
            i += 1
        elif roman[i] == "C" and roman[i + 1] == "M":
            integer_number += (values["M"] - values["C"])
            i += 2
        elif roman[i] == "M":
            integer_number += values["M"]
            i += 1
        elif roman[i] == "C" and roman[i + 1] == "D":
            integer_number += (values["D"] - values["C"])
            i += 2
        elif roman[i] == "C":
            integer_number += values["C"]
            i += 1
        elif roman[i] == "L":
            integer_number += values["L"]
            i += 1
        elif roman[i] == "X" and roman[i + 1] == "C":
            integer_number += (values["C"] - values["X"])
            i += 2
        elif roman[i] == "X" and roman[i + 1] == "L":
            integer_number += (values["L"] - values["X"])
            i += 2
        elif roman[i] == "X":
            integer_number += values["X"]
            i += 1
        elif roman[i] == "V":
            integer_number += values["V"]
            i += 1
        elif roman[i] == "I" and roman[i + 1] == "X":
            integer_number += (values["X"] - values["I"])
            i += 2
        elif roman[i] == "I" and roman[i + 1] == "V":
            integer_number += (values["V"] - values["I"])
            i += 2
        elif roman[i] == "I":
            integer_number += values["I"]
            i += 1
        else:
            i += 1

print(integer_number)

# method - 2
# i = 0
# while i <= (len(roman) - 1):
#     if roman[i] == "D":
#         integer_number += 500
#         i += 1
#     elif roman[i] == "C" and roman[i + 1] == "M":
#         integer_number += (1000 - 100)
#         i += 2
#     elif roman[i] == "M":
#         integer_number += 1000
#         i += 1
#     elif roman[i] == "C" and roman[i + 1] == "D":
#         integer_number += (500 - 100)
#         i += 2
#     elif roman[i] == "C":
#         integer_number += 100
#         i += 1
#     elif roman[i] == "L":
#         integer_number += 50
#         i += 1
#     elif roman[i] == "X" and roman[i + 1] == "C":
#         integer_number += (100 - 10)
#         i += 2
#     elif roman[i] == "X" and roman[i + 1] == "L":
#         integer_number += (50 - 10)
#         i += 2
#     elif roman[i] == "X":
#         integer_number += 10
#         i += 1
#     elif roman[i] == "V":
#         integer_number += 5
#         i += 1
#     elif roman[i] == "I" and roman[i + 1] == "X":
#         integer_number += (10 - 1)
#         i += 2
#     elif roman[i] == "I" and roman[i + 1] == "V":
#         integer_number += (5 - 1)
#         i += 2
#     elif roman[i] == "I":
#         integer_number += 1
#         i += 1
#     else:
#         i += 1
#
# print(integer_number)