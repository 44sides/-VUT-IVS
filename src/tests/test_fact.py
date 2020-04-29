## @file test_fact.py
# @brief Tests of the fact() function from math_library
# @see math_library.Math_library

from src.math_library import Math_library as m
import pytest

def test_fact() :
    result = m.fact(3)
    assert result == 6
    
def test_fact_neg() :
    with pytest.raises(ValueError) :
        result = m.fact(-3)

def test_fact_zero() :
    result = m.fact(0)
    assert result == 1

def test_fact_zero_float() :
    with pytest.raises(ValueError) :
        result = m.fact(0.25)

def test_fact_float() :
    with pytest.raises(ValueError) :
        result = m.fact(8.99)

