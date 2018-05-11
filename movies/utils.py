
class ToRomanError(Exception): pass
class OutOfRangeError(ToRomanError): pass
class NotIntegerError(ToRomanError): pass

ROMAN_NUMERAL_TABLE = (
    ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),  ("IX", 9),   ("V", 5),   ("IV", 4),
    ("I", 1)
)

def to_roman(number):
    """ Convert an integer to Roman
    >>> print(convert_to_roman(45))
    XLV """
    
    if not (0 < number):
        raise OutOfRangeError("number must be non-negative")
    
    if int(number) != number:
        raise NotIntegerError("cannot convert decimals")
    
    roman_numerals = []
    for numeral, value in ROMAN_NUMERAL_TABLE:
        count = number // value
        number -= count * value
        roman_numerals.append(numeral * count)

    return ''.join(roman_numerals)