from src.math_library import Math_library as m
import pytest
import math

def test_root() :
    result = m.root(64)
    assert result == math.sqrt(64)

def test_root() :
    result = m.root(555)
    assert result == math.sqrt(555)

def test_root_neg() :
    with pytest.raises(ValueError) :
        result = m.root(-55)

def test_root_zero() :
    result = m.root(0)
    assert result == 0