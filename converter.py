"""
This function works by attempting to subract by the respective amount of
each roman numeral to the input number.
"""
def decimal_to_roman_numeral(number: int):
    if number == 0:
        return ""
    roman_numeral = ""
    # This checks if the roman numeral should have an M
    while number - 1000 >= 0:
        number -= 1000
        roman_numeral += "M"
    # This checks to see if it should use CM
    while number - 900 >= 0:
        number -= 900
        roman_numeral += "CM"
    # This checks for D
    while number - 500 >= 0:
        number -= 500
        roman_numeral += "D"

    while number - 400 >= 0:
        number -= 400
        roman_numeral += "CD"

    while number - 100 >= 0:
        number -= 100
        roman_numeral += "C"

    while number - 90 >= 0:
        number -= 90
        roman_numeral += "XC"

    while number - 50 >= 0:
        number -= 50
        roman_numeral += "L"

    while number - 40 >= 0:
        number -= 40
        roman_numeral += "XL"

    while number - 10 >= 0:
        number -= 10
        roman_numeral += "X"

    while number - 9 >= 0:
        number -= 9
        roman_numeral += "IX"

    while number - 5 >= 0:
        number -= 5
        roman_numeral += "V"

    while number - 4 >= 0:
        number -= 4
        roman_numeral += "IV"

    while number - 1 >= 0:
        number -= 1
        roman_numeral += "I"
    
    return roman_numeral

"""
This function works by checking the roman numeral input string from left to right
adding up the values of each of the characters as it goes.
Because of the nature of letters that can subtract others,
it checks pairs of letters first, and then moves on to single characters.
"""
def roman_numeral_to_decimal(roman_numeral: str):
    number = 0
    while len(roman_numeral) > 0:
        if roman_numeral[:2] == "CM":
            number += 900
            roman_numeral = roman_numeral[2:]

        elif roman_numeral[:2] == "CD":
            number += 400
            roman_numeral = roman_numeral[2:]

        elif roman_numeral[:2] == "XC":
            number += 90
            roman_numeral = roman_numeral[2:]

        elif roman_numeral[:2] == "XL":
            number += 40
            roman_numeral = roman_numeral[2:]

        elif roman_numeral[:2] == "IX":
            number += 9
            roman_numeral = roman_numeral[2:]

        elif roman_numeral[:2] == "IV":
            number += 4
            roman_numeral = roman_numeral[2:]

        elif roman_numeral[0] == "M":
            number += 1000
            roman_numeral = roman_numeral[1:]

        elif roman_numeral[0] == "D":
            number += 500
            roman_numeral = roman_numeral[1:]

        elif roman_numeral[0] == "C":
            number += 100
            roman_numeral = roman_numeral[1:]

        elif roman_numeral[0] == "L":
            number += 50
            roman_numeral = roman_numeral[1:]

        elif roman_numeral[0] == "X":
            number += 10
            roman_numeral = roman_numeral[1:]

        elif roman_numeral[0] == "V":
            number += 5
            roman_numeral = roman_numeral[1:]

        elif roman_numeral[0] == "I":
            number += 1
            roman_numeral = roman_numeral[1:]

        else:
            raise RuntimeError("Invalid input")
        
    return number
