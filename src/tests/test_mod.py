from src.math_library import Math_library as m
import pytest

def test_mod() :
    result = m.mod(558, 221)
    assert result == 558 % 221

def test_mod_float() :
    result = m.mod(558, 2)
    assert result == 558 % 2.

def test_mod_float_2() :
    result = m.mod(558.444, 221.1)
    assert result == 558.444 % 221.1

def test_mod_zero() :
    with pytest.raises(ZeroDivisionError) :
        result = m.mod(558, 0)