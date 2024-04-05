from converter import *


should_loop: bool = True
list_of_integers: list[str] = [str(i) for i in range(10)]

print("Please enter a number or roman numeral. Type 'exit' to leave the program.")
while should_loop:
    value = 0
    value = input("Input: ")
    if value == 'exit':
        break
    try:
        # This if statement converts the value to an integer if decimal is the input
        if value[0] in list_of_integers:
            value = int(value)

        if type(value) == int:
            if value == 0:
                print("Zero doesn't exist in Roman Numerals")
            else:
                print('The value is: ' + decimal_to_roman_numeral(value))
        else:
            print('The value is: ' + str(roman_numeral_to_decimal(value)))
    except:
        print("Invalid Input.")