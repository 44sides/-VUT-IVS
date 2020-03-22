from src.math_library import Math_library as m
import pytest

def test_ln() :
    result = m.ln(math.e)
    assert result == 1

def test_ln_default_value() :
    result = m.ln(math.e ** 2)
    assert result == 2

def test_ln_neg() :
    with pytest.raises(ValueError) :
        result = m.ln(-3)

def test_ln_zero() :
    with pytest.raises(ValueError) :
        result = m.ln(0)