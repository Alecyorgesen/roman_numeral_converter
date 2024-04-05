def decimal_to_roman_numeral(number):
    roman_numeral = ""
    # This checks if the roman numeral should have an M
    if number - 1000 >= 0:
        number -= 1000
        roman_numeral += "M"
    # This checks for D
    if number - 500 >= 0:
        number -= 500
        roman_numeral += "D"