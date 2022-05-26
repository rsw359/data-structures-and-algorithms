# Roman Numerals

The challenge here is to create a function that can take roman numeral numbers characters and convert them to integers and return the total number.

## Approach & Efficiency

The approach is to create a dictionary that can be used to traslate roman numbers into integers, and then a separate function that compares walks through the numbers and compares them to determine whether the value should be added or subtracted from the following number.

## Time Complexity

The Time Complexity for this algorithm grows along with the amount of data elements making it: O(N)

[Code](../../code_challenges/roman_numerals.py)

[Tests](../../tests/code_challenges/test_roman_numerals.py)
