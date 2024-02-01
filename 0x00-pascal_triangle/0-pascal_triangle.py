#!/usr/bin/python3
"""
Function pascal triangle
"""


def pascal_triangle(n):
    """Print Pascal's Triangle
        n (int): Size of the pascal triangle
    """
    t = []
    if (n <= 0):
        return t
    else:
        for i in range(n+1):
            p = []
            c = 1
            for j in range(1, i+1):
                p.append(c)
                c = c * (i - j) // j
            if (len(p)):
                t.append(p)
    return t
