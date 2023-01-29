from important_program import roman

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
# Developer intent, part 5. Properties

# Domain, expert. Why oh why this?
# Domain, expert. Real and real boundaries. Both >3999 and simplified Roman numerals.

# References. Answers aren't as simple as you think.

from assertpy import soft_assertions, assert_that

def test_four_is_IV():
    with soft_assertions():
        #assert_that(roman(4)).is_equal_to('IIII')
        assert_that(roman(4)).is_equal_to('IV')

def test_snapshot():
    assert_that(roman(4)).snapshot(id='roman of 4')


import hypothesis.strategies as st
from hypothesis import given

SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

@given(st.integers(min_value=1, max_value=3999))
def test_all_numerals_in_set_of_roman_numerals(num):
    numeral = roman(num)
    assert set(numeral) and set(numeral) <= set(SYMBOLS.keys())

@given(numeral_value=st.sampled_from(tuple(SYMBOLS.items())))
def test_generate_numerals_in_symbols(numeral_value):
    numeral, value = numeral_value
    assert roman(value) == numeral

SUBTRACTIVE_SYMBOLS = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

@given(numeral_value=st.sampled_from(tuple(SUBTRACTIVE_SYMBOLS.items())))
def test_generate_subtractive_numerals(numeral_value):
    numeral, value = numeral_value
    assert roman(value) == numeral



