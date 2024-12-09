import math
from typing import Tuple, Literal

def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    Checks if three sides can form a valid triangle.
    A triangle is valid if the sum of any two sides is greater than the third side.
    """
    return a + b > c and a + c > b and b + c > a

def triangle_type(a: float, b: float, c: float) -> Literal["Equilateral", "Isosceles", "Scalene", "Not a triangle"]:
    """
    Determines the type of triangle based on its sides.
    Returns 'Equilateral', 'Isosceles', 'Scalene', or 'Not a triangle'.
    """
    if not is_valid_triangle(a, b, c):
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def triangle_area(a: float, b: float, c: float) -> float:
    """
    Calculates the area of a triangle using Heron's formula.
    Returns the area or raises a ValueError if the triangle is invalid.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle dimensions")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def triangle_perimeter(a: float, b: float, c: float) -> float:
    """
    Calculates the perimeter of a triangle.
    Returns the perimeter or raises a ValueError if the triangle is invalid.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle dimensions")
    return a + b + c

def is_right_triangle(a: float, b: float, c: float) -> bool:
    """
    Checks if a triangle is a right triangle using the Pythagorean theorem.
    """
    if not is_valid_triangle(a, b, c):
        return False
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# New Functions

def triangle_angles(a: float, b: float, c: float) -> Tuple[float, float, float]:
    """
    Calculates the angles (in degrees) of a triangle using the law of cosines.
    Returns a tuple of the three angles.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle dimensions")
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return angle_a, angle_b, angle_c

def triangle_height(base: float, a: float, b: float, c: float) -> float:
    """
    Calculates the height of the triangle corresponding to a given base.
    Uses the area and the base to determine the height.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle dimensions")
    area = triangle_area(a, b, c)
    return 2 * area / base

def inscribed_circle_radius(a: float, b: float, c: float) -> float:
    """
    Calculates the radius of the circle inscribed in a triangle.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle dimensions")
    area = triangle_area(a, b, c)
    s = (a + b + c) / 2
    return area / s

def circumscribed_circle_radius(a: float, b: float, c: float) -> float:
    """
    Calculates the radius of the circumscribed circle of a triangle.
    """
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle dimensions")
    area = triangle_area(a, b, c)
    return (a * b * c) / (4 * area)
