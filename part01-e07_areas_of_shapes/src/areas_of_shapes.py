#!/usr/bin/env python3

import math

def calculate_triangle_area(a, b):
    return 0.5 * a * b

def calculate_rectangle_area(a, b):
    return a * b

def calculate_circle_area(a):
    return math.pi * a**2


def main():
    # enter you solution here
    while(True):
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if not shape:
            break

        if shape.lower() == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = calculate_triangle_area(base, height)

        elif shape.lower() == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = calculate_rectangle_area(width, height)

        elif shape.lower() == "circle":
            radius = float(input("Give radius of the circle: "))
            area = calculate_circle_area(radius)
        
        else:
            print("Unknown shape!")
            continue
        
        print(f"The area is {area:.6f}")
            


if __name__ == "__main__":
    main()
