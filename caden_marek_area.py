import math


# Gets the area for a circle and checks for errors
def area_circle(radius):
    if type(radius) != int and type(radius) != float:
        raise TypeError('Not numeric input')

    if radius <= 0:
        raise ValueError('Not positive')

    return 'Circle area = ', math.pi * (radius ** 2)


# Gets the area for a rectangle and checks for errors
def area_rectangle(length, width):
    if (type(length) != int or type(width) != int) and (type(length) != float and type(width) != float):
        raise TypeError('Not numeric input')

    if length <= 0 or width <= 0:
        raise ValueError('Not positive')

    return 'Rectangle area = ', length * width


# Gets the area for a square and checks for errors
def area_square(side):
    if type(side) != int and type(side) != float:
        raise TypeError('Not numeric input')

    if side <= 0:
        raise ValueError('Not positive')

    return 'Square area = ', side * side


# Gets the area for a triangle and checks for errors
def area_triangle(base, height):
    if (type(base) != int or type(height) != int) and (type(base) != float and type(height) != float):
        raise TypeError('Not numeric input')

    if base <= 0 or height <= 0:
        raise ValueError('Not positive')

    return 'Triangle area = ', (base * height) * .5
