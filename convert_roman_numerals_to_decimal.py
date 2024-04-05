from converter import *

input_file_name: str = input("Enter input file name: ")
output_file_name: str = input("Enter output file name: ")

with open(input_file_name, 'r') as file:
    lines = file.readlines()

with open(output_file_name, 'w') as file:
    for line in lines:
        number_as_string = str(roman_numeral_to_decimal(line.strip()))
        file.write(number_as_string)
        file.write('\n')