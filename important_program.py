# Program, that converts numbers to Roman numbers.

def  roman (num):
     if   not (0 < num < 4000 ):
         raise   ValueError ('number out of range (must be 1..3999)')
     if   not   isinstance (num, int):
         raise   TypeError ('non-integers can not be converted')
     ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
     nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
     result   =   []
     for i in range (len(ints)):
         count = int(num / ints[i])
         result . append (nums[i] * count)
         num -= ints[i] * count
     return ''. join (result)

import pytest

@pytest.mark.parametrize("num, expected", [(4, 'IV'), (2, "II"),(2023, "MMXXIII"),(1, "I"),(3999, "MMMCMXCIX") ])
def test_roman_converter(num, expected):
    assert roman(num) == expected

@pytest.mark.parametrize("num", [0, 4000, -1])
def test_error(num):
    with pytest.raises(ValueError):
        roman(num)

# Bug: True as input
def test_locking_boolean_input_():
    '''Locking test for current incorrect functionality. True should raise TypeError.
    Instead True is treated as one. This test fails when we fix the implementation to match intent.'''
    assert roman(True) == 'I'

@pytest.mark.parametrize("num", [1.5, "hello", (1, 2), None])
def test_error2(num):
    with pytest.raises(TypeError):
        roman(num)

from helpers.numeral_ref import NumeralRefPage as r

def test_ref(browser_page):
    assert r(browser_page).numeral_ref(3999) == 'MMMCMXCIX'


# Checklist of things NOT INCLUDED in the tests so far:

# Developer intent, part 4. Sampling vs wide nets (approvals)

# Domain, expert. Why oh why this?
# Domain, expert. Real and real boundaries. Both >3999 and simplified Roman numerals.

# References. Answers aren't as simple as you think.

from assertpy import soft_assertions

def test_four_is_IV():
    with soft_assertions():
        assert roman(4) == 'IV'
        assert roman(4) == 'IIII'