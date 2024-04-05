# roman_numeral_converter
The main file runs a loop that let's you input decimal numbers or roman numerals
and converts the value to the other and prints it in the terminal.

You can end the program by typing 'exit'.

There are 2 other files that you can run. You can run 'convert_roman_numerals_to_decimal'. It asks for an input file upon running, as well as an output file. The input should only have roman_numerals in it of the correct syntax, and the output will the the decimal numbers listed on each line.

The 'convert_decimal_to_roman_numerals' acts exactly as the other, but instead it converts decimal numbers into roman numerals and outputs the roman numerals on each line of the output file.

Some things to note is that if you input values larger that 3999, it doesn't reject it, but rather it
outputs roman numerals based on what the value should be theoreticaly if it were allowed to use more M's.
Also, certain inputs it will still accept even if the letters are swapped in ways they are not allowed to be.
For example, MI will output 1001 and IM will also output 1001.
