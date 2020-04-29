## @file math_library.py
# @brief Implementation of own math. library
# @post Library begins to be tested
# @package CalculatorPack


## @class Math_library
# @brief Own math. operations
class Math_library(object):

    ## @brief Adding
    @staticmethod
    def add(x, y):
        return x + y

    ## @brief Subtraction
    @staticmethod
    def sub(x, y):
        return x - y

    ## @brief Multiplying
    @staticmethod
    def mul(x, y):
        return x * y

    ## @brief Division
    @staticmethod
    def div(x, y):
        return x / y

    ## @brief Factorial
    @staticmethod
    def fact(x):
        if x < 0:
            raise ValueError
            return 0
        elif x == 0 or x == 1:
            return 1
        else:
            fact = 1
            while x > 1:
                fact *= x
                x -= 1
            if 0 < x < 1:
                raise ValueError
                return
            return fact

    ## @brief Common root
    @staticmethod
    def n_root(x, y):
        r_pow = Math_library.div(1, y)
        return x ** r_pow

    ## @brief Power
    @staticmethod
    def pow(x, y):
        return x ** y
