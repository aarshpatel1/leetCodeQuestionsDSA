# question - 13 (Roman to Integer)

roman = input("Enter the Roman Number: ").upper()
values = {
    "I": "1",
    "V": "5",
    "X": "10",
    "L": "50",
    "C": "100",
    "D": "500",
    "M": "1000"
}

integer_number = ""
valid_number = True
for i in roman:
    if i not in values:
        valid_number = False
        break

roman += "N"

if valid_number:
    for i in range(len(roman)):
        if roman[i] == "M":
            integer_number = str(int(integer_number) + int(values["M"]))
        elif roman[i] == "D":
            integer_number = str(int(integer_number) + int(values["D"]))
        elif roman[i] == "C" and roman[i + 1] == "M":
            integer_number = str(int(integer_number) - int(values["C"]) + int(values["M"]))
        elif roman[i] == "C" and roman[i + 1] == "D":
            integer_number = str(int(integer_number) - int(values["C"]) + int(values["D"]))
        elif roman[i] == "C":
            integer_number = str(int(integer_number) + int(values["C"]))
        elif roman[i] == "L":
            integer_number = str(int(integer_number) + int(values["L"]))
        elif roman[i] == "X" and roman[i + 1] == "C":
            integer_number = str(int(integer_number) - int(values["X"]) + int(values["C"]))
        elif roman[i] == "X" and roman[i + 1] == "L":
            integer_number = str(int(integer_number) - int(values["X"]) + int(values["L"]))
        elif roman[i] == "X":
            integer_number = str(int(integer_number) + int(values["X"]))
        elif roman[i] == "I" and roman[i + 1] == "X":
            integer_number = str(int(integer_number) - int(values["I"]) + int(values["X"]))
        elif roman[i] == "I" and roman[i + 1] == "V":
            integer_number = str(int(integer_number) - int(values["I"]) + int(values["V"]))
        elif roman[i] == "I":
            integer_number = str(int(integer_number) + int(values["X"]))

        #
        # elif roman[i] == "I" and roman[i + 1] == "V":
        #     integer_number += str(int(values["V"]) - int(values["I"]))
        # elif roman[i] == "I" and roman[i + 1] == "X":
        #     integer_number += str(int(values["X"]) - int(values["I"]))
        # elif roman[i] == "I" and roman[i + 1] == "I" and roman[i + 2] == "I":
        #     integer_number += str(int(values["I"]) * 3)
        # elif roman[i] == "I" and roman[i + 1] == "I":
        #     integer_number += str(int(values["I"]) * 2)
        # elif roman[i] == "I":
        #     integer_number += values["I"]

print(integer_number)