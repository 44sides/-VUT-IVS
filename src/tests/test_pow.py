## @file test_pow.py
# @brief Tests of the pow() function from math_library
# @see math_library.Math_library

from src.math_library import Math_library as m
import pytest
import math

def test_pow() :
    result = m.pow(558, 2)
    assert result == math.pow(558, 2)

def test_pow_neg() :
    result = m.pow(558, -2)
    assert result == math.pow(558, -2)

def test_pow_zero() :
    result = m.pow(558, 0)
    assert result == math.pow(558, 0)
