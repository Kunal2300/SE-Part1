import math


class Calculator():
        
    def add(cls,x, y):
        """Add Function"""
        return x + y


    def subtract(cls,x, y):
        """Subtract Function"""
        return x - y


    def multiply(cls,x, y):
        """Multiply Function"""
        return x * y


    def divide(cls,x, y):
        """Divide Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x / y
    
    def floor_division(cls,x,y):
        """Floor Division Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x //y

    def power(cls, x,y):
        """Power of number Function"""
        return x**y

    def factorial(cls,x):
        """Function to find factorial"""
        fact=1
        if(x==0 or x==1):
            return 1
        else:
            return math.factorial(x)
