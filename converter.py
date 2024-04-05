# This function works by attempting to subract by the respective amount of
# each roman numeral to the input number.
def decimal_to_roman_numeral(number):
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


