#!/usr/bin/env python3
from fractions import Fraction

class Rational(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def __add__(self, other):
        add_fraction = Fraction(Fraction(self.v1, self.v2) + Fraction(other.v1, other.v2))
        return Rational(add_fraction.numerator, add_fraction.denominator)
    
    def __sub__(self, other):
        add_fraction = Fraction(Fraction(self.v1, self.v2) - Fraction(other.v1, other.v2))
        return Rational(add_fraction.numerator, add_fraction.denominator)
    
    def __mul__(self, other):
        add_fraction = Fraction(Fraction(self.v1, self.v2) * Fraction(other.v1, other.v2))
        return Rational(add_fraction.numerator, add_fraction.denominator)
    
    def __truediv__(self, other):
        add_fraction = Fraction(Fraction(self.v1, self.v2) / Fraction(other.v1, other.v2))
        return Rational(add_fraction.numerator, add_fraction.denominator)
    
    def __eq__(self, other):
        return Fraction(self.v1, self.v2) == Fraction(other.v1, other.v2)

    def __lt__(self, other):
        return Fraction(self.v1, self.v2) < Fraction(other.v1, other.v2)
    
    def __gt__(self, other):
        return Fraction(self.v1, self.v2) > Fraction(other.v1, other.v2)
    
    def __str__(self):
        return f"{self.v1}/{self.v2}"


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
