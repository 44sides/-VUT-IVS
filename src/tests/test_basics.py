## @file test_basics.py
# @brief Tests of the basic math functions function from math_library
# @see math_library.Math_library

from src.math_library import Math_library as m
import pytest

def test_add() :
    result = m.add(558, 221)
    assert result == 558 + 221

def test_add_float() :
    result = m.add(558, 221.)
    assert result == 558 + 221.

def test_add_float_2() :
    result = m.add(558.55, 221.9)
    assert result == 558.55 + 221.9

def test_sub() :
    result = m.sub(558, 221)
    assert result == 558 - 221

def test_sub_float() :
    result = m.sub(558.88, 221)
    assert result == 558.88 - 221

def test_sub_zero() :
    result = m.sub(558, 0)
    assert result == 558 - 0

def test_sub_minus() :
    result = m.sub(558, 1111)
    assert result == 558 - 1111

def test_mul() :
    result = m.mul(558, 221)
    assert result == 558 * 221

def test_mul_float() :
    result = m.mul(558, 221.555)
    assert result == 558 * 221.555

def test_mul_zero() :
    result = m.mul(558, 0)
    assert result == 558 * 0

def test_mul_minus() :
    result = m.mul(558, -55)
    assert result == 558 * -55

def test_div() :
    result = m.div(558, 221)
    assert result == 558 / 221

def test_div_float() :
    result = m.div(558, 2.)
    assert result == 558 / 2.

def test_div_float_2() :
    result = m.div(558.444, 221.1)
    assert result == 558.444 / 221.1

def test_div_zero() :
    with pytest.raises(ZeroDivisionError) :
        result = m.div(558, 0)