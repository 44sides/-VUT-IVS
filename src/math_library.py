import math

class Math_library(object) :

    @staticmethod
    def add(x, y) :
        return x + y
        
    @staticmethod
    def sub(x, y) :
        return x - y
    
    @staticmethod
    def mul(x, y) :
        return x * y
        
    @staticmethod
    def div(x, y) :
        return x / y

    @staticmethod
    def mod(x, y) :
        return x % y

    @staticmethod
    def fact(x) :
        return math.factorial(x)

    @staticmethod
    def root(x) :
        return math.sqrt(x)

    @staticmethod
    def pow(x , y) :
        return math.pow(x, y)

    @staticmethod
    def log(x , y) : 
        return math.log(x , y)

    @staticmethod
    def ln(x):
        return math.log(x, math.e)