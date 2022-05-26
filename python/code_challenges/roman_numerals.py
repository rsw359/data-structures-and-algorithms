from operator import le


def roman_to_arabic(roman):
  roman = roman.upper()
  total = 0
  for  i in range(len(roman)-1):
    left_char =roman[i]
    right_char =roman[i+1]
    left_value = convert_char(left_char)
    right_value = convert_char(right_char)

    if left_value < right_value:
      left_value = - left_value

    total+=left_value

  if roman:
    total += convert_char(roman[-1])

  return total

def convert_char(roman_char):
  conversion_map = {
    'M':1000,
    'D':500,
    'C':50,
    'X':10,
    'V':5,
    'I':1,
  }

  return conversion_map.get(roman_char, 0)
