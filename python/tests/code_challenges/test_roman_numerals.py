from attr import define
from code_challenges.roman_numerals import roman_to_arabic

def test_roman_to_arabic_exists():
  assert roman_to_arabic

def test_short_list():
  roman = "XV"
  actual = roman_to_arabic(roman)
  expected = 15
  assert actual == expected

def test_lowercase_list():
  roman = "xv"
  actual = roman_to_arabic(roman)
  expected = 15
  assert actual == expected

def test_longer_list():
  roman = "MCMLXXIV"
  actual= roman_to_arabic(roman)
  expected = 1974
  assert actual == expected

