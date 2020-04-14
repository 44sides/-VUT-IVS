from src.math_library import Math_library as m
import math
import pytest

def test_log() :
    result = m.log(100, 10)
    assert result == math.log(100, 10)

def test_log_default_value() :
    result = m.log(100)
    assert result == math.log(100, 10)

def test_log_neg() :
    with pytest.raises(ValueError) :
        result = m.log(558, -2)

def test_log_zero() :
    with pytest.raises(ValueError) :
        result = m.log(558, 0)