## @file test_root.py
# @brief Tests of the n_root() function from math_library
# @see math_library.Math_library

from src.math_library import Math_library as m
import pytest
import math

def test_root() :
    result = m.n_root(64, 2)
    assert result == math.sqrt(64)

def test_root_2() :
    result = m.n_root(555, 2)
    assert result == round(math.sqrt(555), 13)

def test_root_neg() :
    with pytest.raises(ValueError) :
        result = m.n_root(-55, 2)

def test_root_neg_2() :
    with pytest.raises(ValueError) :
        result = m.n_root(55, -2)

def test_root_zero() :
    result = m.n_root(2, 0)
    assert result == 0