#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    sol_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    sol_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return (sol_1, sol_2)


def main():
    pass

if __name__ == "__main__":
    main()
