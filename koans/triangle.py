#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    unique_sides = {a, b, c}

    if len(list(filter(lambda x: (x <= 0), unique_sides))) > 0:
        raise TriangleError("LOL!")

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise TriangleError("LOL!")

    triangle_types = {
        1: "equilateral",
        2: "isosceles",
        3: "scalene"
    }

    return triangle_types.get(len(unique_sides))

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
