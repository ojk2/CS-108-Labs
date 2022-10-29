"""CS 108 - Lab 9.1

This program will attempt to implement a class for outputting
fractions given inputs numerator and denominator.


@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""
# Put your solution code here, replacing this line.
import math

class Fraction:
    def __init__(self, numerator, denominator):
        """take in two parameters: numerator, denominator."""
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def is_valid(self):
        if self.denominator == 0:
            return False
        else:
            return True
        
    def get_decimal_value(self):
        return float(f"{self.numerator / self.denominator:.5f}")
    
    def simplify(self):
        gcdself = math.gcd(self.numerator, self.denominator)
        if gcdself != 0:
            self.numerator = self.numerator // gcdself
            self.denominator = self.denominator // gcdself
        if self.denominator < 0:
            self.numerator = self.numerator * -1
            self.denominator = self.denominator * -1
            
    def __mul__(self, other):
        self.other = other
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    
