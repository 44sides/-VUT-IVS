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
        if x < 0:
            raise ValueError
            return 0
        elif x == 0 or x == 1:
            return 1
        else :
            fact = 1
            while(x > 1):
                fact *= x
                x -= 1
            if x > 0 and x < 1:
                raise ValueError
                return
            return fact

    @staticmethod
    def root(x) :
        if x < 0:
            raise ValueError
            return
        return x ** 0.5

    @staticmethod
    def pow(x , y) :
        return x ** y

    @staticmethod
    def log(x, y=10) : 
        return math.log(x , y)

    @staticmethod
    def ln(x):
        return math.log(x, math.e)